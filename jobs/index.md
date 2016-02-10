---
title: Jobs
layout: default
---
<ul class="post-list">

<h1 style="color: #000000;">
</h1>

<h2 style="color: #000000;">
  Work at the Sustainable Engineering Lab
</h2>

<p style="color: #000000;">
  We solve real-world problems in the developing world; we build software to make the development process smarter and to bring new services, like health and energy, to people that need them most. We primarily focus our efforts in Africa, India and Haiti.
</p>

<p style="color: #000000;">
  The problems we tackle are often related to data and data flow; the tools we build incorporate geospatial planning, open-data web services, operational optimization algorithms, mobile phone-based data collection, data dashboards and the like. We use python, R, go, mongodb, nodejs/javascript, but above all, we&#8217;re looking for people who are passionate about software engineering in a development context.
</p>

<p style="color: #000000;">
  <em>Columbia University is an affirmative action/equal opportunity employer. Minorities and women are encouraged to apply.</em>
</p>

<h2 style="font-weight: 500 !important; color: #000000;">
  Current opportunities:
</h2>
  {% for post in site.posts %}
    {%if post.categories contains 'jobs' %}
        <li>
          <h2>
            <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
          </h2>
          <p>{{post.content}}</p>
        </li>
    {% endif %}
  {% endfor %}
</ul>
