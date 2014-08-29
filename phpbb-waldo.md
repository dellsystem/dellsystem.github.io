---
title: phpBB Where's Waldo MOD
layout: mod
topic-url: http://www.phpbb.com/community/viewtopic.php?f=70&t=2092309
repo-name: phpBB-waldo
short-name: waldo
versions:
- {number: 0.0.1, status: ALPHA, notes: First release}
- {number: 0.0.2, status: ALPHA, notes: "Fixing up code to better adhere to standards, some new config settings"}
- {number: 0.0.3, status: ALPHA, notes: "Some small bug fixes (maintenance release)"}
- {number: 0.0.4, status: ALPHA, notes: "More bugfixes from last release, fixed UTF problem in mouseover text"}
- {number: 0.0.5, status: ALPHA, notes: "Another maintenance release - removed reference to unnecessary variable"}
- {number: 0.1.0, status: BETA, notes: "Added some features and better points MOD integration"}
- {number: 0.1.1, status: BETA, notes: "Hide wait time setting in ACP if UPS isn't installed"}
- {number: 0.1.2, status: BETA, notes: "Fixed relative path issues for image source"}
status: BETA
screenshots:
- https://github.com/dellsystem/phpBB-waldo/raw/master/contrib/screenshot-index.png
- https://github.com/dellsystem/phpBB-waldo/raw/master/contrib/screenshot-profile.png
- https://github.com/dellsystem/phpBB-waldo/raw/master/contrib/screenshot-ucp.png
requests-open: true
---

A small image of Waldo \[US\] / Wally \[UK\] may appear somewhere on every page as you browse the board. Inspired by Xore's 2.x MOD CamelMOD.

## Features

* The probability of appearance, mouseover text, hyperlink and the URL to the image are all adjustable through the ACP
* Integration with the [Ultimate Points MOD](http://www.phpbb.com/customise/db/mod/ultimate_points), so that finding Waldo results in points
* Installable with AutoMOD

**Planned**:

* ACP permissions (issue #1)
* Ability to upload image via ACP (issue #2)
* Ability to cap amount of points earned in a time period (issue #3)
* Ability to enable/disable feature for guests/groups (issue #4)
* Ability to exclude or set pages on which Waldo can appear (issue #5)
* Ability to configure when points should be awarded (issue #6)
