---
title: Jobs
---
<ul class="post-list" style="margin:0px">

<h1 style="color: #000000;">
</h1>

<h2 style="color: #000000;">
  Work at the Quadracci Sustainable Engineering Lab
</h2>

<p style="color: #000000;">
  We solve real-world problems in the developing world; we use engineering to make the development process smarter and to bring new services, like health and energy, to people that need them most. 
</p>

<p style="color: #000000;">
  <em>Columbia University is an affirmative action/equal opportunity employer. Minorities and women are encouraged to apply.</em>
</p>


    <h2 style="font-weight: 500 !important; color: #000000;">
      Current opportunities:
    </h2>

    {% if site.categories.jobs %}
      {% for post in site.categories.jobs %}
          <h1>
            {{ post.title }}
          </h1>
          <p>{{post.content}}</p>
      {% endfor %}
    {% else %}
      <p>There are currently no listings. Please check back soon!</p>
    {% endif %}

</ul>
<h2 style="font-weight: 500 !important; color: #000000;">Projects</h2>
<p style="color: #000000;">Have a look around our site for some of the <a href="/projects/">projects</a> we are working on, and some <a href="/products-tools/">software tools</a> we are building to solve the problems we encounter.</p>
<p style="color: #000000;">Project examples:</p>

<ul style="color: #000000;">
  <li><a href="/shared-solar/">Shared Solar</a> &#8211; Micro-grid solution providing electric infrastructure to a cluster of customers that are not immediately considered viable for grid connectivity.  <a href="/tags/#Shared Solar">See related blog posts</a></li>
  <li><a href="/acacia-irrigation/">Acacia Irrigation</a> &#8211; Smart solar irrigation in Senegal.  <a href="/tags/#Acacia Irrigation">See related blog posts</a></li>
  <li><a href="/quench/">Quench</a> &#8211; Safe drinking water management solution for rural, urban, and peri-urban settings.  <a href="/tags/#Quench">See related blog posts</a></li>
</ul>

<p style="color: #000000;">Tool examples:</p>

<ul style="color: #000000;">
  <li><a href="/network-planner/">Network Planner</a> &#8211; Online tool for planning grid, mini-grid, and off-grid electricity from the community scale to national scale.  <a href="/tags/#Energy Planning">See related blog posts</a></li>
  <li><a href="/dokomo/">Dokomo Forms</a> &#8211; Offline-capable mobile data collection tool.  <a href="/tags/#Dokomo Forms">See related blog posts</a></li>
</ul>

