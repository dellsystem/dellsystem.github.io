---
title: writing
layout: default
---

writing
-------

there is nothing here, not even this line

<ul class="posts">
    {% for post in site.posts %}
        <li><a href="{{ post.url }}">{{ post.title }}</a> ({{ post.date | date_to_string }})</li>
    {% endfor %}
</ul>
