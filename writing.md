---
title: writing
layout: default
---

writing
-------

<p class="meta">there is nothing here, not even this line</p>

<ul class="posts">
    {% for post in site.posts %}
        <li><a href="{{ post.url }}">{{ post.title }}</a> ({{ post.date | date_to_string }}) Category: {{ post.category }}</li>
    {% endfor %}
</ul>
