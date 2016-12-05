---
layout: post
title: "Agora Octave: Update #3"
categories:
- octave
- django
image: socis-2012-with-octave
code: true
---

I've been pretty sick this week and, as a result, haven't managed to get as much done as I would have liked. I did manage to get the new design mostly integrated with Django, and made some changes to it based on [feedback from the mailing list](http://octave.1599824.n4.nabble.com/Feedback-on-Agora-Octave-design-td4642875.html). I've [pushed the commits](http://inversethought.com/hg/hgwebdir.cgi/agora-dellsystem/), but it's still very much a work in progress. There is a demo running at [agora.dellsystem.me](http://agora.dellsystem.me/).

## This week

### Changes to the design

I removed the sombrero graphic from the banner, as it was mentioned that there were too many logos on the front page. I also changed the order of the menu items in the header, from about - code - discuss - help to code - discuss - help - about, again as the result of discussion on the mailing list (although this can be easily changed later on if necessary). The layout, wording, and associated icons of the headings on the front page were changed as well, with the Octave logo replacing the "Share your code" icon.

### Integrating the design into Django's template system

I reorganised the static files directory, creating css/, img/, and js/ subdirectories and temporarily removing all the existing files. I then converted the modified design mockup into HTML, LESS, and image files. Some of the existing pages still need to be styled or have the javascript added back, which I will work on next week.

## Next week

### Finishing up the design integration

Next week, I will convert all the existing pages over to the new design and static file organisation. This will require adding new CSS, Javascript and possibly images, as well as integrating some of the existing code into the new system. I'll also finish the layout of the code-browsing portal and any other pages that need to be finished.

### File upload functionality

After the design integration is complete, I'll work on the code-sharing features (bundle and single-file upload). At the moment I am not completely sure how all the various code-sharing components are related, and what the correct nomenclature should be. I will clarify that with my mentor and will aim to have these components more or less functional by next week.

## Position in timeline

* _**August 1-15:** Check out codebase, get it running; read all the code and documentation; start learning Mercurial_
* **August 16-31: Start working on design; start mocking up models and routes for the components**
* _**September 1 - October 15:** Work on the core components, with as much test coverage and documentation as is feasible; start implementing the views, models and templates_
* _**October 16-31:** Ensure that documentation is thorough and up to date; write any remaining tests that need to be written; test out the user interface and fix any bugs_
