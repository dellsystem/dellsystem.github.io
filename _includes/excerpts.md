{% for post in site.posts limit:10 %}

[{{ post.title }}]({{ post.url }})
----------------

<div class="post">

<a href="{{ post.url }}"><img class="leftfloat" src="/img{% if post.image %}/posts/{{ post.image }}{% else %}{{ post.url }}{% endif %}.png" /></a>

<p>{{ post.date | date_to_string }}</p>

<p>{{ post.content | strip_html | truncate:300 }}</p>

<p class="rightfloat"><a href="{{ post.url }}">Read more &raquo;</a></p>

<p>Categories: {% for category in post.categories %}<strong><a href="/archives#{{ category|replace:' ','-' }}">{{ category }}</a></strong>{% if forloop.last %}{% else %}, {% endif %}{% endfor %}</p>

</div>

{% endfor %}
