---
id: 20
title: Projects
author: Jonathan Carbajal
post-author: jonathan
layout: page
guid: http://modilabs.org/?page_id=20
---

<ul class="post-list">
    {% for post in site.categories.alumni %}
      <li>
        <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}</span>

        <h2>
          <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
        </h2>
      </li>
    {% endfor %}
  </ul>
