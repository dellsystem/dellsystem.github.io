---
layout: default
title: home
---

I'm Wendy Liu, and I'm currently the CTO of [Macromeasures], a data science
startup that I co-founded after graduating from McGill University in 2014.

In case you're wondering about the username: I have no affiliation with Dell
Inc; "dellsystem" is an unfortunate consequence of a decision I made when I was
12, when I signed up for an account on phpbb.com so I could get support for my
phpBB installation.  Since I was using a Dell computer at the time,
"dellsystem" seemed like a reasonable choice for what I thought would be a
throwaway account. I was wrong about the throwaway part, as the phpBB community
turned out to be a gateway drug for open source software and programming in
general. I have since come to terms with the username "dellsystem" and will
even answer to "dell".

Below, you'll find excepts of my most recent blog posts (you can view them all
on the [writing](/writing) page). If you want to get in touch, find me on
Twitter [@dellsystem](https://twitter.com/dellsystem), or check out my [about
page](/about#contact) for other contact options.

[Macromeasures]: http://macromeasures.com

<br />
<hr />
<br />

{% for post in site.posts limit:5 %}
{% include excerpt.html %}
{% endfor %}

<br />
<p class="centered"><a href="/writing">More posts</a></p>
