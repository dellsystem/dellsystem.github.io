---
layout: post
title: "Agora Octave: Update #8"
categories:
- agora
- django
image: socis-2012-with-octave
code: true
---

I made quite a bit of progress on bundle/module uploading this week. A lot of it is behind-the-scenes work, and there are still a few things that need to be done before it's production-ready, so unfortunately I don't have a working demo yet. For a sneak preview of what's coming, check out the screenshots below.

## This week

### Bundles

My main focus was working on the bundle uploading feature. The idea is that you should be able to upload either a plain text file or an archive (zip, tar, etc) containing the files you want to share. If you upload an archive, then it should be unpacked on the server, and the contents of the archive should be restored with their original filenames and directory structure, and shown on the page with syntax highlighting (if possible).

The naive approach to extracting the archive file is to just unpack it immediately after it is uploaded and display the contents of the archive afterwards. However, extracting archive files is something that can take quite a bit of time, particularly for large files. Handling this in the server thread would result in long wait-times and, in the case of a single-threaded server, would prevent others from loading the site at all while a zip file is being extracted. This is, of course, unacceptable for any site that needs to be used in production.

The solution? Using an asynchronous task queue system. I chose [celery](http://celeryproject.org/) because I've used it successfully in previous projects and because it integrates well with Django. Although this definitely increases the complexity of Agora, in terms of deployment, dependencies, and the codebase, it's not really avoidable due to the nature of the functionality that Agora requires. Other ways of executing tasks (like archive extraction) asynchronously, such as using the subprocess module, are simply not feasible because of the post-extraction processing that needs to be done.

The result is that creating a bundle only takes as long as uploading the file. Once the bundle has been created, the user is redirected to the bundle view page. If the file is still being processed, the user will be shown something like this:

!["Still processing" message](http://cs.mcgill.ca/~wliu65/media/agora/bundle-processing.png)

Once the file processing is complete, the message will disappear, and users can view the files in the bundle. If a single plain-text file was uploaded, its contents (with syntax highlighting) will be displayed on the page, along with its filename:

![Single file upload](http://cs.mcgill.ca/~wliu65/media/agora/single-file-upload.png)

If, instead, an archive file containing multiple files were uploaded, then the contents of all the plain-text files (of reasonable length) will be shown instead:

![Bundle, using an archive](http://cs.mcgill.ca/~wliu65/media/agora/bundle-archive.png)

The interface will be very similar to that of snippets, with the main differences being that: 1) filenames (and directory structures) are incorporated; and 2) each bundle can contain multiple "snippets".

### Line numbers revisited

I took another look at using [CSS counters](http://www.quirksmode.org/css/counter.html) for displaying line numbers, which I mentioned briefly in [my last post](/posts/line-numbering/). It turns out that I was incrementing the counter incorrectly last time - instead of doing:

{% highlight css %}
.line:before {
	counter-increment: line;
	content: counter(line);
}
{% endhighlight %}

I should have been doing this:

{% highlight css %}
.line {
	counter-increment: line;
}

.line:before {
	content: counter(line);
}
{% endhighlight %}

(and then resetting the counter for each snippet encountered).

The problem with this technique is that there doesn't appear to be a way to make the line numbers hyperlinks. One way around this is to use Javascript to make the line itself a hyperlink, so that when you click anywhere on a line of code you're taken to the relevant anchor. Of course, this still requires Javascript, so I don't know if it's really a better solution. It's also a bit harder to style. The current implementation (using Javascript to display the line numbers) should suffice for now, so I'm going to table this issue and only come back to it if it turns out there's a major problem with the current method.

## Next week

### Finishing up bundles

Sadly, bundle uploading is far from complete. I haven't committed the changes I've made yet, partly because I had to do a fair bit of restructuring of the way imports are done in order to get celery to work, which seems to have broken the snippet feature. It's also very much a work-in-progress - certainly not stable enough to be used in production - and I want to get it in a more acceptable state, with adequate documentation, before committing it.

Here are some of the things that I am prioritising for next week:

* Updating the README and the requirements file to account for the new dependencies and setup instructions
* Fixing the snippet functionality (it has to do with imports being changed from `from agora.apps.etc import Etc` to `from apps.etc import Etc`, which causes the mptt app to register the Snippet model twice)
* Testing edge cases (empty archive files, different types of compression, maliciously named files, etc)
* Displaying images, and allowing users to download other types of files
* Committing the changes and updating my [demo](http://agora.dellsystem.me)

Some more long-term goals for the bundle feature include:

<a name="bundle-goals"></a>

* Ensuring that file uploading is secure (for instance, it needs to be able to handle [zip bombs](http://en.wikipedia.org/wiki/Zip_bomb) without exploding)
* A bundle management system (so that users can rename, delete, and add files after creating a bundle)
* Downloads (so that users can easily download the contents of a bundle as an archive file)
* Figuring out terminology (bundles, modules or something else entirely?)
* Mercurial integration (eventually)

I'm going to be buried in schoolwork this week, so I won't be able to focus on Agora again until Friday. The plan is to finish up the most important aspects of this feature on Friday, commit, and then start working on the others. There are also some housekeeping changes I'd like to make, so hopefully I'll have time to get to those as well (in terms of improving code organisation and the like).

## Position in timeline

* _**August 1-15:** Check out codebase, get it running; read all the code and documentation; start learning Mercurial_
* _**August 16-31:** Start working on design; start mocking up models and routes for the components_
* **September 1 - October 15: Work on the core components, with as much test coverage and documentation as is feasible; start implementing the views, models and templates**
* _**October 16-31:** Ensure that documentation is thorough and up to date; write any remaining tests that need to be written; test out the user interface and fix any bugs_
