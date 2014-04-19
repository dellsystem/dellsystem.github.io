---
layout: post
title: "Showing only additions and deletions in git"
categories:
- git
code: true
---

If you've ever been in a situation where you wanted to see _only_ the additions,
or _only_ the deletions, in a git diff, then you probably know that it's not as
simple as running `git diff --diff-filter=A` or `git diff --diff-filter=D`. At
least, not if you're looking for added or deleted _lines_, as opposed to files.

From the man page for `git diff`:

<br />

{% highlight groff %}
--diff-filter=[ACDMRTUXB*]

Select only files that are

* A Added
* C Copied
* D Deleted
* M Modified
* [omitted]
{% endhighlight %}

That's pretty cool, but this only works on **files**. So this would let us see
only new files, or only deleted files. But what about lines? What if you only
want to see the lines that have been added (or deleted) in one file?

## The solution

Unfortunately, git does not appear to have an option for this built-in. On the
bright side, if you run a \*NIX system, you can do this:

{% highlight bash %}
git diff | grep ^+
{% endhighlight %}

This gets you all the additions. To see all the deletions:

{% highlight bash %}
git diff | grep ^+
{% endhighlight %}

Note that the output of the first command will also give you something like

{% highlight bash %}
+++ b/filename
{% endhighlight %}

for each affected file. If this is a problem, you can alter the regex to account
for this (or just delete it manually).

You can of course pass other parameters to `git diff`, such as the specific
commit or commit range you want to see the diff for, or the filename(s).

## The use case

So why would anyone ever need to do something like this?

If you've ever been to a [Model United Nations] conference, you probably know
that in exchange for paying a nominal registration fee and giving up your
weekend to try to convince someone (who is not actually a representative of
the United States) that you (someone who is not actually a representative of
Iran) have absolutely no intention of producing nuclear weapons, definitely not,
let's go out for a drink and I'm sure we can clear up this whole
misunderstanding, you get a nice shiny badge that says your name, your school,
and the country that you are supposed to pretend to represent, which looks
something like this:

![expanding acronyms is hard](/img/posts/additions-deletions-git/badpuns.png)

For the last year or so, I was part of the organising committee for a Model
United Nations conference that is [sadly not named BADPUNS][mcmun].
As the USG-IT, one of my responsibilities was to take the registration
information that was provided by conference attendees through the website and
send it to the person in charge of printing badges. Since the website was
[completely custom-built][github] and I didn't feel like writing a ton of code
to make this into an actual feature (since, theoretically, it would only have to
be used once), I just wrote a [simple Django management command][command] for
exporting the information for the badges as a CSV file.

It worked fine, except for the fact that it was a week before the conference and
some of the attendees still had not filled in their names. But we needed to get
at least some of the ~1400 badges printed now, so I sent off what I had, and
those badges got printed.

Two days later, when I exported the new badge list, I used git to figure out the
difference between the current badges.csv and the previous one. The difficulty
arose from the fact that not only did we have new badges to print (because some
attendees didn't fill in their information before), we had badges to get rid of
as well (because some attendees had last-minute cancellations). So I needed to
use the exported badges.csv file to generate a new CSV containing just the new
badges to be printed, as well as one listing the badges to be discarded.

That's where git and grep came to the rescue. To get rid of the + and - at the
beginning of each line, I just used Vim's visual block mode. Much easier than
manually checking each name, which is probably what I would have done if I
didn't have git in my life.

There may actually be a way of doing this with just git, but I haven't found it.
This might be a pretty hacky solution, but hey, it works.

Know of a better solution? Do tell! I'm [@dellsystem] on Twitter.

[Model United Nations]: http://en.wikipedia.org/wiki/Model_United_Nations
[mcmun]: http://www.mcmun.org
[github]: https://github.com/dellsystem/mcmun-2014
[command]: https://github.com/dellsystem/mcmun-2014/blob/master/mcmun/management/commands/get_badge_names.py
[@dellsystem]: https://twitter.com/dellsystem
