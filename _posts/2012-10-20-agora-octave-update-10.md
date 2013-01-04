---
layout: post
title: "Agora Octave: Update #10"
categories:
- agora
- django
image: socis-2012-with-octave
code: true
---

I worked primarily on the bundle feature this week. I added a rudimentary versioning system and made some other smaller changes, including fixing the bundle explore page, making bundle descriptions optional and fixing the 404 and 500 error page templates.

## This week

The full commit log is available here: <http://inversethought.com/hg/hgwebdir.cgi/agora-dellsystem/>

### Bundle versioning and editing

You can now upload a new version of a bundle (either as an archive or as a plain text file - [commit 177](http://inversethought.com/hg/agora-dellsystem/rev/86129d185ddb)). Files in previous versions of the bundle can be accessed by viewing the bundle at a particular version.

You can also now edit the details (currently only the description and license - the name is not editable as it constitutes part of the URL) of a bundle that you are the creator of.

Additionally, bundle descriptions are now optional ([commit 176](http://inversethought.com/hg/agora-dellsystem/rev/c042d26e6936)).

### Smaller changes

* Added help text to name field for bundles, explaining that the name is meant to be a slug (part of the URL) ([commit 171](http://inversethought.com/hg/agora-dellsystem/rev/a57d15b044a7))
* Made form field labels bold ([commit 172](http://inversethought.com/hg/agora-dellsystem/rev/5e10ea8052b5)
* Added the ability to whitelist certain mimetypes that do not begin with `text/` (currently only XML - [commit 179](http://inversethought.com/hg/agora-dellsystem/rev/76abe6d681ea))
* Added number of views to snippet details page ([commit 175](http://inversethought.com/hg/agora-dellsystem/rev/1be4e1229711))
* Added publish date and number of views to snippet explore page ([commit 173](http://inversethought.com/hg/agora-dellsystem/rev/b5e9ad94da00))
* Fixed 404 and 500 error pages (hadn't yet converted the template files over to the new template system - [commit 174](http://inversethought.com/hg/agora-dellsystem/rev/e40d79359d07))

## Next week

### More on bundles

Here's [last week's version](/posts/agora-octave-update-9/), with the completed ones removed:

* Ensuring that file uploading is secure (for instance, it needs to be able to handle zip bombs without exploding)
* Displaying images and allowing downloads for individual files
* Adding license information to uploaded files (see this Perl script)
* Downloads (so that users can easily download the contents of a bundle as an archive file)
* Rating/feedback functionality
* Mercurial integration (eventually)

Here are other things that need to be done:

* Showing the timestamp and an optional comment for new versions of bundles
* Fixing the left bar for listing files in a bundle (if the structure is deeply nested or if the filenames are particularly long, the user will have to scroll horizontally, which can be unwieldy)

### Housekeeping changes

(Continued from last week, since I didn't have time to do this for the entire codebase.) Deleting unused code, making use of Django shortcuts and other conveniences when possible, checking concordance with PEP 8, etc.

## Position in timeline

* _**August 1-15:** Check out codebase, get it running; read all the code and documentation; start learning Mercurial_
* _**August 16-31:** Start working on design; start mocking up models and routes for the components_
* _**September 1 - October 15**: Work on the core components, with as much test coverage and documentation as is feasible; start implementing the views, models and template_
* **October 16-31: Ensure that documentation is thorough and up to date; write any remaining tests that need to be written; test out the user interface and fix any bugs**

(This timeline isn't really relevant anymore, but I'll keep including it for reference.)
