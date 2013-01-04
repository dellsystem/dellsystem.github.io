---
layout: post
title: "Agora Octave: Update #6"
categories:
- agora
- django
image: socis-2012-with-octave
code: true
---

This will be a short update, partly because of the [follow-up update](/posts/agora-octave-update-5-1/) I posted three days ago (which covers most of what I accomplished this week) and partly because school is now in full swing and so I've been spending a lot of time [trying to type up my notes](http://beta.wikinotes.ca/user/dellsystem). Only minor changes this week. I'll definitely do something cool by next week, though, so stay tuned.

## This week

Summary of changes:

* added an emacs pygments style
* fixed some W3C validation errors
* fixed my first merge conflict with hg, using vimdiff (it was a bit scary)

## Next week

### Module upload

I wasn't able to make too much progress on this yet. Next week!

### Profiles

Same as above.

### Ability to upload files as snippets

In the IRC channel, jwe suggested adding the ability to upload a file to be posted as a snippet, in addition to the current method of pasting it into a text box. This sounds like a useful feature, and I will work on that for next week.

### Spam prevention

I'll look into ways of dealing with spam (the old installation at agora.octave.org was flooded with spammy snippets). Jordi suggested not publicly listing anonymous snippets, and requiring a CAPTCHA (possibly using [this app](https://github.com/mbi/django-simple-captcha)) for registration.

## Position in timeline

* _**August 1-15:** Check out codebase, get it running; read all the code and documentation; start learning Mercurial_
* _**August 16-31:** Start working on design; start mocking up models and routes for the components_
* **September 1 - October 15: Work on the core components, with as much test coverage and documentation as is feasible; start implementing the views, models and templates**
* _**October 16-31:** Ensure that documentation is thorough and up to date; write any remaining tests that need to be written; test out the user interface and fix any bugs_
