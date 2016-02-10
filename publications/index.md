---
title: Publications
author: Roger Wong
layout: default
---
<div>
<h1 class="page-heading">Publications</h1>

<div class="col-md-4" style="float:left; margin:0; width:33%;">
  <h2> Infrastructure</h2>
  <ul class="post-list" style="list-style-type:none">
    {% for post in site.posts %}
      {%if post.categories contains 'publications' and post.categories contains 'Infrastructure' %}
          <li>
            <p><strong>
              <a class="post-link" href="{{ post.link }}" target="\_blank">{{ post.title }}</a>
            </strong></p>
            <p>{{post.content}}</p>
          </li>
      {% endif %}
    {% endfor %}
  </ul>
  <h2> Water</h2>
  <ul class="post-list" style="list-style-type:none">
    {% for post in site.posts %}
      {%if post.categories contains 'publications'and post.categories contains 'Water' %}
          <li>
            <p><strong>
              <a class="post-link" href="{{ post.link }}" target="\_blank">{{ post.title }}</a>
            </strong></p>
            <p>{{post.content}}</p>
          </li>
      {% endif %}
    {% endfor %}
  </ul>
</div>
<div class="col-md-4"  style="float:left; margin:0; width:33%;">
  <h2>Energy Planning</h2>
  <ul class="post-list" style="list-style-type:none">
    {% for post in site.posts %}
      {%if post.categories contains 'publications'and post.categories contains 'Energy Planning' %}
          <li>
            <p><strong>
              <a class="post-link" href="{{ post.link }}" target="\_blank">{{ post.title }}</a>
            </strong></p>
            <p>{{post.content}}</p>
          </li>
      {% endif %}
    {% endfor %}
  </ul>

  <h2>Household Energy Usage</h2>
  <ul class="post-list" style="list-style-type:none">
    {% for post in site.posts %}
      {%if post.categories contains 'publications'and post.categories contains 'Household Energy Usage' %}
          <li>
            <p><strong>
              <a class="post-link" href="{{ post.link }}" target="\_blank">{{ post.title }}</a>
            </strong></p>
            <p>{{post.content}}</p>
          </li>
      {% endif %}
    {% endfor %}
  </ul>
</div>

<div class="col-md-4"  style="float:left; margin:0; width:33%;">
  <h2>Data Collection & Analysis</h2>
  <ul class="post-list" style="list-style-type:none">
    {% for post in site.posts %}
      {%if post.categories contains 'publications'and post.categories contains 'Data Collection & Analysis' %}
          <li>
            <p><strong>
              <a class="post-link" href="{{ post.link }}" target="\_blank">{{ post.title }}</a>
            </strong>
            </p>
            <p>{{post.content}}</p>
          </li>
      {% endif %}
    {% endfor %}
  </ul>
</div>

<p class="rss-subscribe">subscribe <a href="{{ "/feed.xml" | prepend: site.baseurl }}">via RSS</a></p>


</div>
