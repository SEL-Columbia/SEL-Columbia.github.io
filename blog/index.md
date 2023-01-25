---
title: Blog
---

<div class="container">
    <strong>Most recent posts</strong>
    <a href="/blog/archive">Blog archive</a>
    {% for post in site.categories.blog limit: 10 %}
        {% include post_summary.html post=post %}
    {% endfor %}
    <strong>Most recent posts</strong>
    <a href="/blog/archive">Blog archive</a>
</div>
