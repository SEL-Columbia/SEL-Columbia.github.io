---
id: 27
title: Blog
author: John Humphrey
layout: page
guid: http://modilabs.org/?page_id=27
---

<div class="row">
  <ul class="post-list">
    {% for post in site.posts %}
        {% if post.categories contains 'blog' %}
      <li>
        <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}</span>

        <h2>
          <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
        </h2>
      </li>
      {% endif %}
    {% endfor %}
  </ul>
</div>