---
layout: post
title: "Agora Octave: Update #4"
categories:
- octave
- django
image: socis-2012-with-octave
code: true
---

Update #4 for Agora Octave. I worked on completing the integration of the snippet functionality with the new design, added the ability to change the syntax highlighting colour scheme, and made some minor housekeeping changes. See below for the exciting details

## This week

### Integrating snippets and the new design

I added back the "view snippet" view, with all of its functionality: "view raw", delete, toggle word-wrapping, line numbers, and syntax highlighting (more on that below). I also made a small change to the lexer field to ensure that when you revise a snippet, the chosen lexer is the same as the lexer for the original snippet, which is probably what you would expect.

### Syntax highlighting colour schemes

There are now 8 different syntax highlighting colour schemes, and you can switch between them when you view a snippet. Most of them are the default stylesheets that come with Pygments, with one being mostly-custom ("vibrant"). [View a demo &raquo;](http://agora.dellsystem.me/snippet/Abgi/) (use the syntax highlighting style dropdown near the top)

### Housekeeping changes

I've been slowly cleaning up the code wherever I can, both to meet [PEP 8](http://www.python.org/dev/peps/pep-0008/) (the de facto coding style guide for Python) and to just simplify or improve the code wherever possible. This week, I made some [changes in the order of imports](http://inversethought.com/hg/agora-dellsystem/rev/a8da60d611f7), made use of [a custom shortcut method on a model](http://inversethought.com/hg/agora-dellsystem/rev/365144dad9d1), fixed some [whitespace issues](http://inversethought.com/hg/agora-dellsystem/rev/5a8f1dece263), and [moved the setting of "choices" for a field from the form to the model](http://inversethought.com/hg/agora-dellsystem/rev/d858aae811d0), for logical reasons and to make it easier to get the human-readable name in any situation. I also upgraded the Django dependency to 1.3, because 1.3 is really quite a bit better (for one, it has the [render](https://docs.djangoproject.com/en/1.3/topics/http/shortcuts/#render) shortcut function, which eliminates the need to manually create a RequestContext).

## Next week

### Profiles

Next week, I will work on completing the profile view as well as the edit profile view, and integrating them with the new style. I'll also add the ability to set a default syntax highlighting colour scheme in your profile that will be applied to all the snippets you view (although it will still be possible to choose a different colour scheme on a per-snippet basis). Additionally, I will work on improving the usability of the login and registration pages by combining them into one, with a window popping up if you have Javascript enabled (sort of like how Reddit does it).

### Code upload

I'll start working on the code upload functionality, for uploading single files as well as bundles. I will also work on the code "explore" view (at /code) - the intention is to create a page that gives a good overview of what is happening around the site, so users can view popular or recently-uploaded code snippets and modules.

## Position in timeline

* _**August 1-15:** Check out codebase, get it running; read all the code and documentation; start learning Mercurial_
* **August 16-31: Start working on design; start mocking up models and routes for the components**
* _**September 1 - October 15:** Work on the core components, with as much test coverage and documentation as is feasible; start implementing the views, models and templates_
* _**October 16-31:** Ensure that documentation is thorough and up to date; write any remaining tests that need to be written; test out the user interface and fix any bugs_
