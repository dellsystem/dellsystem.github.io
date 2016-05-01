{% for post in site.posts %}

[{{ post.title }}]({{ post.url }})
----------------

<div class="post excerpt">

<a href="{{ post.url }}"><img class="leftfloat" src="/img{% if post.image %}/posts/{{ post.image }}{% else %}{{ post.url }}{% endif %}.png" /></a>

<p>{{ post.date | date: "%B %-d, %Y" }}</p>

<p>{{ post.content | strip_html | truncate:400 }}</p>

<p class="rightfloat"><a href="{{ post.url }}">Read more &raquo;</a></p>

<p>Categories: {% for category in post.categories %}<strong><a href="/writing#{{ category|replace:' ','-' }}">{{ category }}</a></strong>{% if forloop.last %}{% else %}, {% endif %}{% endfor %}</p>

</div>

{% endfor %}
