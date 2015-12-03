---
id: 2660
title: Publications
author: Roger Wong
layout: page
guid: 'http://modi.mech.columbia.edu/?page_id=2660'
---
<div>
<h1 class="page-heading">Posts</h1>
<ul class="post-list">
  {% for post in site.posts %}
    {%if post.categories contains 'publications' %}
        <li>
          <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}</span>

          <h2>
            <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
          </h2>
        </li>
    {% endif %}
  {% endfor %}
</ul>

<p class="rss-subscribe">subscribe <a href="{{ "/feed.xml" | prepend: site.baseurl }}">via RSS</a></p>


</div>
