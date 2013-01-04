---
layout: post
title: "Agora Octave: Update #11"
categories:
- agora
- django
image: socis-2012-with-octave
code: true
---

This past week has been full of midterms and assignments so this update will be shorter than usual. I made a few small changes (feature additions and bug fixes) to the bundle feature, mostly based on feedback from the [mailing list](http://octave.1599824.n4.nabble.com/Bundles-in-Agora-td4645137.html).


## This week

The full commit log is available here: <http://inversethought.com/hg/hgwebdir.cgi/agora-dellsystem/>

* If an uploaded bundle contains a file named DESCRIPTION, and the bundle's description is empty, and the bundle is indicated to follow Octave packaging formatting standards, then the contents of that file should be used as the description ([commit 184](http://inversethought.com/hg/agora-dellsystem/rev/b711f0087709), [commit 187](http://inversethought.com/hg/agora-dellsystem/rev/4752861906b3))
* If the user has already created a bundle with the specified name, then the form should display a validation error rather than 500'ing ([commit 183](http://inversethought.com/hg/agora-dellsystem/rev/cdcbfaa65cfe))
* Fixed the submit button text in the bundle form ([commit 182](http://inversethought.com/hg/agora-dellsystem/rev/4a63f5d762a3))

## Next week

I'll continue working on bundles and housekeeping changes (see [last week's update](/posts/agora-octave-update-10/)). I'll also look into documentation integration (suggested by Carlo de Falco via [the mailing list](http://octave.1599824.n4.nabble.com/Bundles-in-Agora-tp4645137p4645583.html)).

In other news, I got an email from ESA a few days ago informing me that I have successfully completed SOCIS 2012. Much thanks to my mentor [Jordi Gutiérrez Hermoso](http://jordi.inversethought.com/) for all of his help as well as the positive feedback. I will continue to work on Agora Octave after the end of the official coding period (which I just realised is tomorrow, making this my last official blog post :() for as long as it takes to get the project in a usable state, although the frequency of my blog posts may decrease as I get closer to exam period. I'm also interested in eventually getting more involved with Octave as a whole, and hopefully even contributing to Octave itself one day &mdash; at the very least, it would be a great opportunity to learn C++. This will probably have to wait until next semester, or at least until I finish my exams (middle/end of December).
