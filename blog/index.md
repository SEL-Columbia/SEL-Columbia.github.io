---
title: Blog
layout: default
---

<div class="container">
    {% for post in site.categories.blog limit: 8%}
        <div class="row">
            <h2>
                <a href="{{ post.url }}">
                    {{ post.title }}
                </a>
            </h2>
            
            <p>
                <span class="article-author">
                    {{ post.author }}
                </span>
                <span class="article-date">
                    {{ post.date | date: "%b %-d, %Y"}}
                </span>
            </p>

            {% comment %}
                http://stackoverflow.com/a/25466298/1475412
            {% endcomment %}
            {% assign images = post.content | split:"<img " %}
            {% for image in images %}
                {% if image contains 'src' %}
                    {% assign attributes = image | split:"/>" | first %}
                    <a href="{{ post.url }}">
                        <img {{attributes}} />
                    </a>
                    {% break %}
                {% endif %}
            {% endfor %}
            
            <p>
                {{ post.content | strip_html | truncatewords: 50 }}
            </p>
        </div>
    {% endfor %}
</div>
