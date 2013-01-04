---
layout: post
title: "Agora Octave: Update #2"
categories:
- agora
- django
image: socis-2012-with-octave
code: true
---

This week, I mainly worked on a mockup for a redesign (available below). I also made some small changes to the readme and pip-requirements, which have been committed.

## This week

### Design mockup

Here's a sneak preview of what I have in mind for the front page (click for higher-resolution):

[![Agora Octave front page sneak preview](http://cs.mcgill.ca/~wliu65/agora_mini.png)](http://cs.mcgill.ca/~wliu65/agora.png)

Things I'm still working on:

* The location of login/logout buttons and other navigation items (for easily accessing the pastebin or code bundles)
* Font for the header (currently Museo Sans - suggestions would be nice)
* Position/size of the Octave sombrero
* The colouring of the logo. I changed the colour to make it fit in more with the icon scheme, but I'm not completely happy with it.
* The layout for logged-in users

I made some small changes to the colour scheme I mentioned last week, partly to better fit the colours used in the Octave logo:

* Dark grey: `#333333`
* Medium grey: `#808080`
* Light grey: `#E6E6E6`
* Dark orange (from the Octave logo; currently not used elsewhere): `#D45500`
* Orange: `#FF7F2A`
* Light blue: `#60CAE1`
* Medium blue: `#22A2CA`
* Dark blue: `#1B749D`

### CSS

I'll be using the [LESS](http://lesscss.org/) CSS preprocessor, with client-side compilation for now. The files will be contained in a css directory within the static files root, and will be organised like this:

* variables.less - the colour scheme, dimensions of major elements, and other variables will be defined here
* mixins.less - will contain mixins for things like vendor-prefixed CSS properties, gradients, and other frequently-used features
* code.less - for the syntax highlighting colour scheme
* agora.less - the main stylesheet file
* imports.less - imports all the other files; is the only file that needs to be included in the HTML

### New dependency: OpenID

I installed [django-openid-auth](http://pypi.python.org/pypi/django-openid-auth/) through pip and added it to the list of dependencies in the readme and in the pip-requirements file. I also updated the readme with instructions on using pip to install all the dependencies.

### Continuous integration

As the result of [this message](http://octave.1599824.n4.nabble.com/Agora-Octave-CSS-preprocessors-and-continuous-integration-tp4642529p4642652.html) on the mailing post, I'm shelving the issue of continuous integration for now. The task of learning how to use Hydra will be left up to [Jordi](http://octave.1599824.n4.nabble.com/template/NamlServlet.jtp?macro=user_nodes&user=224167).

### Basic code maintenance

I'll hold off on this until I actually need to work with the relevant code (i.e. the week after next).

## Next week

### Finishing the design

I'll be spending some more time on the design next week to finish it up and make any necessary improvements. The reason I want to focus on the design so early on is to ensure that the foundation is good, making things much more painless in the long run. If there's a solid, clean, and easily-extensible design framework in place, then adding new pages and features becomes much easier, with immediate visual feedback. Plus, the larger and more complex the project, the harder it becomes to effect a redesign, and so I'm doing it now, while the codebase is still manageable.

### Integrate the design with Django

This entails implementing the design with HTML, CSS and images, and then integrating the HTML files into Django's templating system. The existing pages will be converted over at this stage as well. I'll finish as much as I can by next week's blog post; after next week, I'll start working on adding new features.

## Position in timeline

* _**August 1-15:** Check out codebase, get it running; read all the code and documentation; start learning Mercurial_
* **August 16-31: Start working on design; start mocking up models and routes for the components**
* _**September 1 - October 15:** Work on the core components, with as much test coverage and documentation as is feasible; start implementing the views, models and templates_
* _**October 16-31:** Ensure that documentation is thorough and up to date; write any remaining tests that need to be written; test out the user interface and fix any bugs_
