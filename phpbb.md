---
title: phpBB MODifications
layout: default
---

I am no longer actively developing any of my phpBB MODifications, all of which
were developed for phpBB 3.0x and haven't been ported over to 3.1x. Feel free
to [send me an email](/about) if you have support questions or are interested
in taking over development.

***


## Dynamic Avatar

{::nomarkdown}
{% include phpbb-download.html repo="waldo" %}
{:/nomarkdown}

<img src="/img/phpbb/dynamo.png" class="leftfloat" />

This MOD provides the ability to personalise your avatar, using bodily features
and clothes that can be purchased or acquired. In the vein of 2.0x/3.0x MODs
like Live Avatar, Nulavatar, and [Camorea Suite][camorea].

[View development topic][dynamic-avatar-topic] ::
[View source on Github][dynamic-avatar-github] ::
[Installation guide][dynamic-avatar-install]

### Features

* Everything is controlled from the ACP
* The MOD includes sample images, items and layers for you to play with to
  get the hang of things (all penguin-based)
* Integration with the [Ultimate Points MOD][points], enabling items to be
  purchased
* Installable with AutoMOD

### Screenshots

{::nomarkdown}
{% include phpbb-screenshots.html repo="dynamic-avatar" images="acp-edit-layer,acp-items,acp-layers,acp-settings,edit-avatar-hat" %}
{:/nomarkdown}

***

## Where's Waldo

<img src="/img/phpbb/waldo.png" class="leftfloat" />

{::nomarkdown}
{% include phpbb-download.html repo="waldo" %}
{:/nomarkdown}

A small image of Waldo (US) / Wally (UK) may appear somewhere on every page as
you browse the board. Inspired by [Xore's 2.x MOD CamelMOD][camelmod].

[View development topic][waldo-topic] :: [View source on GitHub][waldo-github]

### Features

* The probability of appearance, mouseover text, hyperlink and the URL to the image are all adjustable through the ACP
* Integration with the [Ultimate Points MOD](http://www.phpbb.com/customise/db/mod/ultimate_points), so that finding Waldo results in points
* Installable with AutoMOD

### Screenshots

{::nomarkdown}
{% include phpbb-screenshots.html repo="waldo" images="index,profile,ucp" %}
{:/nomarkdown}

***

## Multilingual Forums

{::nomarkdown}
{% include phpbb-download.html repo="multilingual-forums" %}
{:/nomarkdown}

<img src="/img/phpbb/multiling.png" class="leftfloat" />

Enables basic multi-language support for forum names and descriptions. Created
as a result of [this MOD
request](https://www.phpbb.com/community/viewtopic.php?f=72&t=2215701).

[View development topic][multilingual-forums-topic] ::
[View source on GitHub][multilingual-forums-github]

### Features

* Custom delimiter, configurable via the ACP (defaults to #)
* Can support any number of languages (as long as they're already installed as
  language packs)

### Screenshots

{::nomarkdown}
{% include phpbb-screenshots.html repo="multilingual-forums"
images="forum,category,acp,language,french,english,index" %}
{:/nomarkdown}

[camelmod]: https://www.phpbb.com/community/viewtopic.php?t=120691
[camorea]: https://www.phpbb.com/community/viewtopic.php?f=434&t=1019935
[waldo-github]: https://github.com/dellsystem/phpBB-waldo
[waldo-topic]: http://www.phpbb.com/community/viewtopic.php?f=70&t=2092309
[dynamic-avatar-topic]: http://www.phpbb.com/community/viewtopic.php?f=70&t=1823845
[dynamic-avatar-github]: https://github.com/dellsystem/phpBB-dynamic-avatar
[dynamic-avatar-install]: https://github.com/dellsystem/phpBB-dynamic-avatar/wiki/Installation-guide
[multilingual-forums-topic]: https://www.phpbb.com/community/viewtopic.php?f=70&t=2231436
[multilingual-forums-github]: https://github.com/dellsystem/phpBB-multilingual-forums
[points]: http://www.phpbb.com/customise/db/mod/ultimate_points/
