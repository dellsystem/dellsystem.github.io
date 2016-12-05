---
layout: post
title: "Simulating the night sky with CSS"
categories:
- web-design
code: true
css: stars
---

Have you ever looked up at the sky on a clear, moonless night? When all you can see is an endless field of stars, glittering like an array of celestial diamonds speckled across a cosmic fabric? Did it make you think, "I wonder if I could simulate this in the browser using transparent images and CSS"?

That has never happened to me either, actually. But it was the best segue into this subject that I could think of.

Recently, I built the [frontend](http://xmas2012.networkdynamics.org/) for a visualisation of Christmas wishes on Twitter. My biggest consideration when thinking of a design was that I wanted to make it somewhat Christmas-themed while avoiding kitschiness as much as possible. I settled on a night sky backdrop, with falling snowflakes simulated using a modified version of [this jQuery plugin](https://github.com/loktar00/JQuery-Snowfall) (okay, a little kitschy, but I'd like to think it embodies a certain classiness as well). The backdrop ended up looking like this:

<div id="stars"><div class="large"></div><div class="medium"></div><div class="small"></div></div>

It looks simple enough, but the technique is actually rather involved. Why? Because the sky is meant to expand to fill the user's browser. Creating a fixed-size image containing randomly-positioned stars would not suffice, because then that image would either have be tiled (which would be very noticeable, ruining the illusion of the endless starfield) or stretched (which could result in very large and pixellated stars for users with larger screens). Neither solution is desirable.

So what's the alternative, if you want to preserve the illusion that these stars go on forever without having to actually generate an endless starfield? My solution was to separate the stars into three different layers: small stars, medium stars, and large stars. Each layer would be a mostly-transparent PNG image, with white dots for stars. And most importantly, the widths and heights of each layer would have to be relatively prime.

In my original design (the one pictured above uses images that are half the size of the original ones, for illustration purposes), the dimensions were:

* Small stars layer: 1103 wide × 541 high
* Medium stars layer: 1009 wide × 479 high
* Larger stars layer: 1051 wide × 524 high

How many pixels of "randomness" do we get before it repeats? Well, all the numbers except 524 are prime, and we can see immediately that 541, 479 and 524 are relatively prime. So the non-repeating area has a width of 1103 × 1009 × 1051 = 1,169,686,277 pixels (the lcm of the individual widths), and a height of 541 × 479 × 524 = 135,788,836. The result is more than hundred million pixels of vertical scroll space and more than a billion pixels of horizontal scroll space before we encounter a pattern of stars that we've seen before. Not bad for less than 14KB of images. (In fact, these numbers are a lot higher than they need to be - anything above 300 or 400 pixels would probably work just as well, with the period being well over a million pixels.)

So that's the basic idea. DesignFestival calls this [the cicada principle](http://designfestival.com/the-cicada-principle-and-why-it-matters-to-web-designers/), which is a catchy if somewhat silly name for something that is a basic property of numbers (there are some really cool examples [here](http://designfestival.com/cicada/)). If you want to use this concept in your own project, the HTML structure looks like this:

{% highlight html %}
<div id="stars">
    <div class="large"></div>
    <div class="medium"></div>
    <div class="small"></div>
</div>
{% endhighlight %}

Feel free to grab the [CSS](/css/posts/stars.css) and the images ([stars_large.png](/img/posts/night-sky-css/stars_large.png), [stars_medium.png](/img/posts/night-sky-css/stars_medium.png), [stars_small.png](/img/posts/night-sky-css/stars_small.png)), though making your own images is pretty fun as well (I spent a few minutes pasting white dots at random positions in an image document in Inkscape; it was a blast). If you do use this in your own project, I would love to [hear about it](/about#contact).
