---
author: viktor-roytman
title: A Library for Portier with asyncio
tags:
  - Software
---

Originally published at https://www.viktorroytman.com/blog/2017/02/15/a-library
-for-portier-with-asyncio/

In [a previous post][pre], I said:

>Down the line, there will be client-side Portier libraries (or, at least,
>other demo implementations) for various languages. Until then, you’ll need to
>do some of the heavy lifting yourself.

Well, I decided to [self-fulfill this prophecy][ful]. Introducing&hellip; the
[asyncio-portier][asp] Python library!

<!--more-->

### Usage

The asyncio-portier library works with Python 3.5 and up.

There's a [functioning demo][dem] included with the library which you can use
as a template. I'll go into more detail about it here.

If you've read the previous post, this should seem pretty familiar. There are a
few important differences though; I'll point them out along the way.

#### The login endpoint

Assuming that

- `cache` is a Redis connection object as from [redis-py][rds]
- `self.audience` is the URL of your application (such as
`https://www.example.com`)
- `broker_url` is the URL of the Portier Broker, `https://broker.portier.io`

{% highlight python %}
from datetime import timedelta
from urllib.parse import urlencode
from uuid import uuid4
import tornado.web

class LoginHandler(tornado.web.RequestHandler):
    def post(self):
        nonce = uuid4().hex
        next_page = self.get_argument('next', '/')
        expiration = timedelta(minutes=15)
        cache.set('portier:nonce:{}'.format(nonce), next_page, expiration)

        query_args = urlencode({
            'login_hint': self.get_argument('email'),
            'scope': 'openid email',
            'nonce': nonce,
            'response_type': 'id_token',
            'response_mode': 'form_post',
            'client_id': self.audience,
            'redirect_uri': self.audience + '/verify'})
        self.redirect(broker_url + '/auth?' + query_args)
{% endhighlight %}

The primary difference here is in what we set in the Redis cache. We prepend
the string `'portier:nonce:'` to the nonce value used for the key, and we set
the value to the `next` URL query parameter. With this, if the user visits a
page that requires authentication, the application can redirect them directly
to that page after they have logged in.

#### The verify endpoint

Assuming that

- You have a template for an error page named `'error.html'`

{% highlight python %}
from asyncio_portier import get_verified_email
import tornado.web

class VerifyHandler(tornado.web.RequestHandler):
    async def post(self):
        error = self.get_argument('error', None)
        if error is not None:
            description = self.get_argument('error_description', None)
            msg = 'Broker Error ({})'.format(error)
            if description is not None:
                msg += ': {}'.format(description)
            self.set_status(400)
            self.render('error.html', error=msg)
            return

        token = self.get_argument('id_token')

        try:
            email, next_page = await get_verified_email(
                broker_url,
                token,
                self.audience,
                broker_url,
                cache)
        except ValueError as exc:
            self.set_status(400)
            self.render('error.html', error=exc)
            return

        self.set_secure_cookie(
            'user_email', email, httponly=True,
            # We're not using HTTPS on localhost, but we would otherwise
            secure=False,
        )
        self.redirect(next_page)
{% endhighlight %}

The `get_verified_email` function now takes a number of explicit parameters
instead of reading from a global `SETTINGS` object. It can raise `ValueError`
instead of `RuntimeError`. It also now returns a `next_page` in addition to an
`email` which, as mentioned before, allows the application to redirect the user
directly to the requested page.

### Wrapping up

This library should make things a little bit easier for anyone using Portier
and asyncio. Please let me know if you run into any [issues][iss]!

[pre]: https://www.viktorroytman.com/blog/2017/01/23/using-portier-with-pythons-asyncio
[ful]: https://en.wikipedia.org/wiki/Self-fulfilling_prophecy
[asp]: https://pypi.python.org/pypi/asyncio-portier
[gve]: https://www.viktorroytman.com/blog/2017/01/23/using-portier-with-pythons-asyncio/#getverifiedemailgve
[dem]: https://github.com/vr2262/asyncio-portier/tree/master/demos/tornado
[rds]: https://github.com/andymccurdy/redis-py
[iss]: https://github.com/vr2262/asyncio-portier/issues
