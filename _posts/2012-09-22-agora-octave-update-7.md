---
layout: post
title: "Agora Octave: Update #7"
categories:
- agora
- django
image: socis-2012-with-octave
code: true
---

This week, I added the ability to edit your account settings, and the ability to upload a file to create a snippet. I've been overloaded with assignments lately (hence the late update) and wasn't able to spend much time on the module upload feature, so I'll have to push that back again. It will be my top priority for next week, though, so stay tuned.

Also, I regenerated my private key and the new public key hasn't yet been updated on the server hosting the [mercurial repository](http://inversethought.com/hg/hgwebdir.cgi/agora-dellsystem/), so I wasn't able to push my changes there. As a temporary workaround, I've exported the commit history to git and pushed it to github: <https://github.com/dellsystem/agora-octave>

## This week

### Ability to upload files as snippets

This feature works pretty well so far. There is a small issue in terms of handling binary files uploads, at least if you're running SQLite (this shouldn't happen with production databases). I implemented a temporary fix for this by checking the `content-type` header of the uploaded file. However, this can be changed by the user, so it's not completely trustworthy, as explained in the [Django documentation](https://docs.djangoproject.com/en/dev/topics/http/file-uploads/?from=olddocs#django.core.files.uploadedfile.UploadedFile.content_type). Unfortunately it looks as if there is no foolproof way to detect the encoding a file in Python, according to [this StackOverflow post](http://stackoverflow.com/questions/436220/python-is-there-a-way-to-determine-the-encoding-of-text-file/436299#436299). I will continue to look into this, though.

[View a demo &raquo;](http://agora.dellsystem.me/snippet/)

### Profiles

You can now edit your profile details. I cleaned up the view code a bit and replaced the manual form processing with the use of a ModelForm.

## Next week

### Module upload

My priority for next week.

### More profile stuff

I believe there are some other user-specific settings (font size, line height?) that users should be able to edit from their profile page. Also, the URL for the editprofile view should probably be changed to something other than /users/editprofile, or else anyone who registers an account with the username "editprofile" will never be able to view his own profile.

### Spam prevention

I will work on implementing the techniques mentioned [last week](/posts/agora-octave-update-6/).

## Position in timeline

* _**August 1-15:** Check out codebase, get it running; read all the code and documentation; start learning Mercurial_
* _**August 16-31:** Start working on design; start mocking up models and routes for the components_
* **September 1 - October 15: Work on the core components, with as much test coverage and documentation as is feasible; start implementing the views, models and templates**
* _**October 16-31:** Ensure that documentation is thorough and up to date; write any remaining tests that need to be written; test out the user interface and fix any bugs_
