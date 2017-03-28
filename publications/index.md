---
title: Publications
author: roger-wong
---
<div>
  <h2 id="products__tools">Publications</h2>

  <div class="span4" style="float:left; margin:0; width:33%;">
    <h3>Infrastructure</h3>
    <ul class="post-list" style="list-style-type:none">
      {% for post in site.categories.publications %}
	{%if post.tags contains 'Infrastructure' %}
	    {% include publication_listing.html post=post %}
	{% endif %}
      {% endfor %}
    </ul>
    <h3>Household Energy Usage</h3>
    <ul class="post-list" style="list-style-type:none">
      {% for post in site.categories.publications %}
  {%if post.tags contains 'Household Energy Usage' %}
      {% include publication_listing.html post=post %}
  {% endif %}
      {% endfor %}
    </ul>
    <h3>Water</h3>
    <ul class="post-list" style="list-style-type:none">
      {% for post in site.categories.publications %}
  {%if post.tags contains 'Water' %}
      {% include publication_listing.html post=post %}
  {% endif %}
      {% endfor %}
    </ul>
  </div>

  <div class="span4"  style="float:left; margin:0; width:33%;">
    <h3>Energy Planning</h3>
    <ul class="post-list" style="list-style-type:none">
      {% for post in site.categories.publications limit: 25 %}
	{%if post.tags contains 'Energy Planning' %}
	    {% include publication_listing.html post=post %}
	{% endif %}
      {% endfor %}
    </ul>
  </div>

  <div class="span4"  style="float:left; margin:0; width:33%;">
    <h3>Energy Planning</h3>
    <ul class="post-list" style="list-style-type:none">
      {% for post in site.categories.publications offset: 25 %}
	{%if post.tags contains 'Energy Planning' %}
	    {% include publication_listing.html post=post %}
	{% endif %}
      {% endfor %}
    </ul>
    <h3>Data Collection & Analysis</h3>
    <ul class="post-list" style="list-style-type:none">
      {% for post in site.categories.publications %}
	{%if post.tags contains 'Data Collection' %}
	    {% include publication_listing.html post=post %}
	{% endif %}
      {% endfor %}
    </ul>
  </div>

</div>
