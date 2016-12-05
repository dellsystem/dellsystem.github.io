---
layout: post
title: "Agora Octave: Update #9"
categories:
- octave
- django
image: socis-2012-with-octave
code: true
---

Lots of progress on the bundle feature this week. I also significantly revised my plans for the feature, based on some very helpful [feedback](http://octave.1599824.n4.nabble.com/Bundles-in-Agora-td4645137.html) from the mailing list. Some other smaller changes - bug fixes, minor feature additions, cosmetic changes - were committed as well.

## This week

### Bundles, continued

I've committed all the progress I've made over the past couple of weeks on bundles. See [commit 151](http://inversethought.com/hg/agora-dellsystem/rev/c7be7def8b57). It's still incomplete, but most of the basic functionality is there. Feel free to [test it out for yourself](http://agora.dellsystem.me/bundles/).

### Optimising dynamic line-number insertion

The dynamic line-number insertion was extraordinarily slow for long snippets. Optimising it was pretty simple, though - I just had to minimise the number of DOM manipulations and to change the `$.each()` call to a standard for loop (see [commit 141](http://inversethought.com/hg/agora-dellsystem/rev/2a2078bd334c)). I should really have done this from the beginning, but at the time I thought that the initial method was neater and that performance wouldn't be an issue, which turned out to be very naive.

### LESS compilation

I added server-side LESS compilation as an option ([commit 143](http://inversethought.com/hg/agora-dellsystem/rev/7a27b1c9cb84)). To trigger it, set `compile_less = yes` in agora.conf. Now, stylesheets load faster, still work with Javascript turned off, and aren't cached in `localStorage` when you don't want them to be.

### Contributions sidebar for user profiles

There is now a sidebar on user profile pages showing what snippets and bundles that user has created ([commit 152](http://inversethought.com/hg/agora-dellsystem/rev/9294cf4097d8)).

### Fixing registration

There was a bug in registration before relating to an incorrect usage of the django-registration app. It should be fixed now ([commit 160](http://inversethought.com/hg/agora-dellsystem/rev/a5547f079190)).

### Other cosmetic changes

Minor cosmetic changes include:

* Adding `word-wrap: break-word` to diffs and snippets (so that extremely long words don't break out of the box - commits [158](http://inversethought.com/hg/agora-dellsystem/rev/d14822d10833) and [161](http://inversethought.com/hg/agora-dellsystem/rev/10eebb5a1c68))
* Adding `overflow-x` to the snippet history list in the sidebar, to ensure that it never gets too cramped ([commit 145](http://inversethought.com/hg/agora-dellsystem/rev/ee999b9f33f5))
* Adding a top margin to the diff box to ensure that it is aligned with the sidebar ([commit 146](http://inversethought.com/hg/agora-dellsystem/rev/6573617409e2))
* Preventing the browser from trying to jump to # when you click the "Highlight code" link ([commit 142](http://inversethought.com/hg/agora-dellsystem/rev/c3c4aaccbcd0))

## Next week

### More on bundles

Here's a revised version of [the to-do list for bundles from last week](/posts/agora-octave-update-8#bundle-goals):

* Ensuring that file uploading is secure (for instance, it needs to be able to handle [zip bombs](http://en.wikipedia.org/wiki/Zip_bomb) without exploding)
* Displaying images and allowing downloads for individual files
* Whitelist for certain mimetypes (e.g., XML) that don't begin with `text/` but should still be considered plain text
* Versioning (the ability to upload subsequent versions of a bundle, each associated with a single incrementing version number)
* Adding license information to uploaded files (see [this Perl script](http://sourceforge.net/p/octave/code/11207/tree/trunk/octave-forge/admin/copyright_fix.pl))
* Downloads (so that users can easily download the contents of a bundle as an archive file)
* Rating/feedback functionality
* Mercurial integration (eventually)

I'll be working on the downloads feature first, then versioning and licensing. I'll probably also come up with other small features while working on these.

### Housekeeping changes

Deleting unused code, making use of Django shortcuts and other conveniences when possible, checking concordance with PEP 8, etc.

## Position in timeline

* _**August 1-15:** Check out codebase, get it running; read all the code and documentation; start learning Mercurial_
* _**August 16-31:** Start working on design; start mocking up models and routes for the components_
* **September 1 - October 15: Work on the core components, with as much test coverage and documentation as is feasible; start implementing the views, models and templates**
* _**October 16-31:** Ensure that documentation is thorough and up to date; write any remaining tests that need to be written; test out the user interface and fix any bugs_

(This timeline isn't really relevant anymore, but I'll keep including it for reference.)
