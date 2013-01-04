---
layout: post
title: "Agora Octave: Update #1"
categories:
- agora
- django
image: socis-2012-with-octave
code: true
---

This week, I read more about the specifications and code for Agora Octave and started investigating some of the solutions. I also made my first few commits to the [Mercurial repository](http://inversethought.com/hg/agora-dellsystem/) (most were minor changes involving settings.py).

## This week

### Reading specifications and code

To get a better understanding of the project, I spent some time reading and re-reading the [current README file](http://inversethought.com/hg/agora/file/9c1e26cc80e3/README), the [somewhat spartan wiki page](http://wiki.octave.org/Agora), and the code (all the .py files). I also read through this [recap of Agora-related discussion during OctConf 2012](http://octave-forge.blogspot.ca/2012/08/octconf2012-agora-and-pkg.html), which was brought to my attention via the mailing list. 

### Changes to settings.py

Most of the edits were whitespace-related (changing 2-space indentation to 4-space indentation, adding/removing it in accordance with [PEP 8](http://www.python.org/dev/peps/pep-0008/), etc). 

There was also a small compatibility issue with Django 1.4 that I experienced when I first tried to run it, which I fixed in [this commit](http://inversethought.com/hg/agora-dellsystem/rev/06b69000a057). More information on that can be found [here](http://blog.madpython.com/2010/04/07/django-context-processors-best-practice).

### Managing dependencies with pip

[pip](http://www.pip-installer.org/en/latest/index.html) is a widely used package installer for Python. It has a great system for managing [project-wide dependencies](http://www.pip-installer.org/en/latest/requirements.html), and works very well in conjunction with [virtualenv](http://www.virtualenv.org/en/latest/index.html).

To get the list of required dependencies, I first set up a virtual environment with virtualenv and then installed all the required modules through pip. I then exported the requirements to a file named `requirements.txt` with `pip freeze > requirements.txt`, as is often the convention (the file was later [renamed](http://inversethought.com/hg/agora-dellsystem/rev/4a32aabcae88) to `pip-requirements`, which does look nicer).

Installing the required dependencies is then a simple matter of running `pip install -r pip-requirements`. This system is especially useful when operating within a virtualenv in which only the default Python modules (and pip) are installed.

### Mercurial

Before making my first commit, I read through the [Mercurial commit message guidelines on the Octave wiki](http://wiki.octave.org/Commit_message_guidelines). They seemed pretty similar to the conventions I use for git, so I didn't have any problems there. One thing that I found somewhat unsettling at first was the lack of output colours, but enabling the colour extension was a simple matter of adding

{% highlight yaml %}
[extensions]
color =
{% endhighlight %}

to my ~/.hgrc, so that was fine.

## Next week

### OpenID for authentication

It was brought up on the [mailing list](http://octave.1599824.n4.nabble.com/Agora-s-design-tp4632088p4632089.html) that we should use openID for authentication. Luckily, there are many libraries for accomplishing this in Django - [this StackOverflow answer](http://stackoverflow.com/questions/2123369/whats-the-best-solution-for-openid-with-django#answer-2184521) suggests that [django-openid-auth](https://launchpad.net/django-openid-auth) is a good choice. Available uner the BSD license, like some of the current dependencies. Next week I try it out, and if it all goes well I will add it to the dependencies.

### Design mockup

For next week's update, I'll include some mockups (images, maybe a static webpage) of redesign proposals. The theme will be consistent with Octave's - `#D45500` (orange), `#0791C1` (blue), `#808080` (grey) - as well as the light grey used in the logo (`#EEEEEC`). I'll also send it out to the mailing list for feedback.

### Continuous integration

My initial plan for ensuring that unit tests are run regularly, against multiple version of Django and Python, was to use the continuous integration tool [Travis](http://www.travis-ci.org). However, since it integrates exclusively with Github, I sent an [email](http://octave.1599824.n4.nabble.com/Agora-Octave-CSS-preprocessors-and-continuous-integration-td4642529.html) to the octave-maintainers mailing list about other possibilities. [Hydra](http://hydra.nixos.org/project/gnu) (a paper about it is available [here](http://nixos.org/~eelco/pubs/hydra-scp-submitted.pdf)) was brought up. Next week, I'll look into it more to see if it's the right tool for the job.

### Updating the readme

I'll edit the readme to reflect the improved dependency management system with pip and the new `pip-requirements` file, and will ensure that the to-do list is up-to-date.

### Basic code maintenance

When reading through the existing code, I noticed some areas that could be improved, as well as some minor organisation and whitespace-related changes that could be made. I'll make any such changes next week.

## Position in timeline

* **August 1-15: Check out codebase, get it running; read all the code and documentation; start learning Mercurial**
* _**August 16-31:** Start working on design; start mocking up models and routes for the components_
* _**September 1 - October 15:** Work on the core components, with as much test coverage and documentation as is feasible; start implementing the views, models and templates_
* _**October 16-31:** Ensure that documentation is thorough and up to date; write any remaining tests that need to be written; test out the user interface and fix any bugs_
