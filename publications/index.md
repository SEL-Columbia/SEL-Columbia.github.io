---
title: Publications
author: roger-wong
---

<div>
  <h2 id="products__tools">Publications</h2>

  <div class="span4" style="float:left; margin:0; width:49%;">
    <h3>Innovations in Electricity Access</h3>
    <ul class="post-list" style="list-style-type:none">
      {% for post in site.categories.publications %}
	      {%if post.tags contains 'Innovations in Electricity Access' %}
	        {% include publication_listing.html post=post %}
	      {% endif %}
      {% endfor %}
    </ul>
    <h3>LED Lighting</h3>
    <ul class="post-list" style="list-style-type:none">
      {% for post in site.categories.publications %}
	      {%if post.tags contains 'LED Lighting' %}
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
    <h3>Drinking Water</h3>
    <ul class="post-list" style="list-style-type:none">
      {% for post in site.categories.publications %}
        {%if post.tags contains 'Drinking Water' %}
          {% include publication_listing.html post=post %}
        {% endif %}
      {% endfor %}
    </ul>
    <h3>Cookstoves</h3>
    <ul class="post-list" style="list-style-type:none">
      {% for post in site.categories.publications %}
        {%if post.tags contains 'Cookstoves' %}
          {% include publication_listing.html post=post %}
        {% endif %}
      {% endfor %}
    </ul>
    <h3>Geospatial Planning</h3>
    <ul class="post-list" style="list-style-type:none">
      {% for post in site.categories.publications %}
        {%if post.tags contains 'Geospatial Planning' %}
          {% include publication_listing.html post=post %}
        {% endif %}
      {% endfor %}
    </ul>
  </div>

  <div class="span4"  style="float:left; margin:0; width:49%;">
    <h3>ICT Energy & Infrastructure</h3>
    <ul class="post-list" style="list-style-type:none">
      {% for post in site.categories.publications %}
	      {%if post.tags contains 'ICT Energy' %}
	        {% include publication_listing.html post=post %}
	      {% endif %}
      {% endfor %}
    </ul>
    <h3>Millennium Development Goals</h3>
    <ul class="post-list" style="list-style-type:none">
      {% for post in site.categories.publications %}
	      {%if post.tags contains 'Development Goals' %}
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
    <h3>Natural Gas</h3>
    <ul class="post-list" style="list-style-type:none">
      {% for post in site.categories.publications %}
        {%if post.tags contains 'Natural Gas' %}
          {% include publication_listing.html post=post %}
        {% endif %}
      {% endfor %}
    </ul>
    <h3>Renewable Integration</h3>
    <ul class="post-list" style="list-style-type:none">
      {% for post in site.categories.publications %}
        {%if post.tags contains 'Renewable Integration' %}
          {% include publication_listing.html post=post %}
        {% endif %}
      {% endfor %}
    </ul>
  </div>

  <h3><a href="https://scholar.google.com/citations?hl=en&user=yIectxQAAAAJ">Google Scholars Profile</a></h3>

</div>
