---
title: About
layout: default
---

<div class="row">
  <div class="col-md-9 col-lg-6 col-sm-12"> 
    <h2>Mission</h2>
    <p>The Sustainable Engineering Lab at the School of Engineering (SEAS) and The Earth Institute, Columbia University uses engineering to help address development issues. We engineer software solutions to help make development planning smarter and to improve the delivery of critical services like health and energy in the developing world.</p> 
  </div>
</div>


<!-- Current Members (team) -->

<div class="row-fluid">
  <div class="span9">
    <h2>
      Team
    </h2> The Lab brings together a diverse set of talents who work in collaboration to engineer solutions to development issues. From designers who understand user needs and talented software engineers to development practitioners and researchers, the expertise at the lab is both broad and deep.
  </div>
</div>

{% for member in site.categories.team reversed %}
{% cycle 'add rows': '<div class="row">', nil, nil, nil %}
<div class="col-md-3">
    <div class="media">
        <a class="pull-left" href="{{ member.url }}">
        <img class="media-object" src="{{ member.photo }}">
        </a>
        <div class="media-body">
            <div class="head media-heading"><a href="{{ member.url }}" class="off">{{ member.full_name}}</a></div>
            <p class="note">{{ member.title }}</p>
        </div>
    </div>
</div>    
{% cycle 'close rows': nil, nil, nil, '</div>' %}
{% endfor %}
{% cycle 'close rows': nil, '</div>', '</div>', '</div>' %}

<!-- Alumni -->

<div class="row-fluid">
  <div class="span9">
    <h2>
      Alumni 
    </h2>  </div>
</div>

{% for alum in site.categories.alumni reversed %}
<div class="row">
    <div class="col-md-2">
        {{ alum.full_name }}
    </div>
    <div class="col-md-2">
        {{ alum.employer }}
    </div>
</div>

{% endfor %}
<div class="row">
  <div class="col-md-9 col-lg-6 col-sm-12"> 
    <h2>Partners</h2>
    <p>
      We work with diverse partners, ranging from small non-profit organizations to large government bodies, mainly working in the developing world.
    </p>
    <ul>
      <li>Office of the Senior Special Assistant to the President on Millennium Development Goals, Nigeria — Nigeria MDGs Information System, Formhub, Facilities Inventory</li>
      <li><a href="http://frhsindia.org/">Foundation for Research in Health Systems</a>, <a href="http://who.int/">World Health Organization</a>, National Rural Health Mission, Karnataka — Drishti</li>
      <li><a href="http://www.millenniumvillages.org/">The Millennium Villages Project</a> — Formhub, ChildCount, Facilities Inventory</li>
      <li><a href="http://www.africasoils.net/">Africa Soil Information System (AfSIS)</a>, <a href="http://africasoils.net/EthiopiaSoils">Ethiopia Soil Information System (EthioSIS)</a> — Formhub</li>
      <li>Kenyan and Senegalese electricity utilities (KPLC and SENELEC) in conjunction with Ministry of Energy in Kenya and the Rural Electrification Agency in Senegal (ASER) has mplemented Network Planner for national level electricity planning.</li>
      <li><a href="http://internews.org/">Internews</a> — Formhub, <a href="http://innovation.internews.org/pilots/project/humanitarian-toolkit">Humanitarian Data Toolkit</a></li>
    </ul>
  </div>
</div>



