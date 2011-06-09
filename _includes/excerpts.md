{% for post in site.posts %}

[{{ post.title }}]({{ post.url }})
----------------

<div class="post">

<a href="{{ post.url }}"><img class="leftfloat" src="/images{{ post.url }}.png" /></a>

<p>{{ post.date | date_to_string }}</p>

<p>{{ post.content | strip_html | truncate, 400 }}</p>

<p>Categories: <strong>{{ post.categories | array_to_sentence_string }}</strong></p>

<p class="rightfloat"><a href="{{ post.url }}">Read more &raquo;</a></p>

</div>

{% endfor %}
