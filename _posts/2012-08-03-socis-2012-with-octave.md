---
layout: post
title: SOCIS 2012 with Agora Octave
categories:
- octave
- django
---

This summer, I'll be working with [Octave](http://www.gnu.org/software/octave) as part of the European Space Agency's [Summer of Code in Space 2012](http://sophia.estec.esa.int/socis2012/). My focus will be on completing <a href="http://agora.octave.org">Agora Octave</a>, which is a code submission and collaboration website for Octave-related projects built using the <a href="https://www.djangoproject.com/">Django web framework</a>.

I'm very excited about the opportunity to work on Agora Octave. I love building websites, especially with Django, and this will be a fun project for me that hopefully will also be of benefit to the Octave community. I've identified the major components  that I will be working on this summer, and have sketched out a rough timeline of when I expect to complete the various steps, which you can find below.

## Project components

### Mercurial integration

When uploading a bundle of code, a user should have the option to either create an associated hg repository or import an existing one. I've never worked with Mercurial before, so I will have to spend some time familiarising myself with it and determining the best way to integrate it with Django.

### User authentication system

A user authentication system is required to ensure that only registered users contribute code, comments, and rankings. This can be done by making use of the built-in `auth` module in Django as well as the [django-registration](http://bitbucket.org/ubernostrum/django-registration) module. Much of this component has already been done.

### Bundle upload and code highlighting

This would be the main feature in Agora. Users should be able to share their code (either as a snippet, or as a bundle) under a particular license, with syntax highlighting done using [Pygments](http://pygments.org). Parts of this component have already been completed.

### Comment system

A comment system is needed to allow authenticated users to post comments on bundles and code snippets. This will be accomplished using the [django-threadedcomments](https://github.com/HonzaKral/django-threadedcomments) module.

### User interface

I plan to develop a clean, consistent, and usable user interface for the website. I will be using [LESS](http://lesscss.org/) for the stylesheets (with server-side compilation) and will create any necessary graphics using [Inkscape](http://inkscape.org).

### Unit tests

Since there are some features with potentially complicated interactions, I will make sure that any code whose validity isn't readily apparent is thoroughly tested. If the need arises, I will also use the continuous integration system [Travis](http://travis-ci.org/), in order to ensure that tests are always run.

### Documentation

I will endeavour to keep my code as well-documented as possible without going overboard, in the form of inline comments, docstrings, notes in the README, and external documentation if need be.

## Timeline

* **August 1-15:** Check out codebase, get it running; read all the code and documentation; start learning Mercurial
* **August 16-31:** Start working on design; start mocking up models and routes for the components
* **September 1 - October 15:** Work on the core components, with as much test coverage and documentation as is feasible; start implementing the views, models and templates
* **October 16-31:** Ensure that documentation is thorough and up to date; write any remaining tests that need to be written; test out the user interface and fix any bugs

## Progress updates, code snapshots, and a mirror

I plan to write a new blog post every Friday with a brief summary of my progress so far. Although I'll be committing my code primarily to a [Mercurial repository](http://inversethought.com/hg/agora-dellsystem/), I will also mirror the repository on [Github](https://github.com/dellsystem/agora-octave) because I like Github's user interface and the tools it provides.

I plan to develop locally, but will make my changes publicly available at [agora.dellsystem.me](http://agora.dellsystem.me).

## About me

I'm an undergraduate student going into my third year towards a Bachelor of Science in Math and Computer Science at McGill University, in Canada. I first started using (and fell in love with) Django last summer, and have been creating and designing websites for about 8 years (of progressively better quality). I've been involved in open source since I joined the [phpBB](http://www.phpbb.com) team in 2007, initially as a moderator, and now as part of the website team as well. I love web design and development, and am currently working part-time for [a music technology lab at McGill](http://ddmal.music.mcgill.ca/) in which I write software and design interfaces.

You can find out more about my projects at [www.dellsystem.me](http://dellsystem.me).
