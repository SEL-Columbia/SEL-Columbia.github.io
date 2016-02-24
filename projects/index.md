---
id: 20
title: Projects
author: Jonathan Carbajal
post-author: jonathan
layout: default
guid: http://modilabs.org/?page_id=20
---

{% for post in site.categories.projects %}
<div class="row-fluid projects">
    <div class="col-sm-12">
        {{ post.excerpt }}
    </div>
    <div class="col-sm-12 projects-details">
        <h3>{{ post.title }}</h3>
        <p><a href="{{ post.url | prepend: site.baseurl }}">Read more</a></p>
    </div>
</div>
{% endfor %}
