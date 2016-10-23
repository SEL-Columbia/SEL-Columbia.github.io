---
title: 'Products &#038; Tools'
---
## While working on projects that create positive impact in the developing world, we produce open tools: {#products__tools}
{% for post in site.categories.products-tools %}
<div class="row-fluid products">
  <div class="span12">
    <div class="row-fluid">
      <div class="span4">
        <a href="{{post.image-link}}">
          <img src="{{post.image-source}}" width="{{post.image-width}}" 
           height="{{post.image-height}}" class="alignnone size-full" />
        </a>
      </div>
      <div class="span8">
        {{ post.content }}
      </div>
    </div>
  </div>
</div>
{% endfor %}
