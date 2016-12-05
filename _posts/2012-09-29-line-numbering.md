---
layout: post
title: "Line numbering is actually surprisingly hard"
categories:
- octave
- web-design
image: line-numbering
code: true
---

Let me share with you a little tale involving line numbers.

One of the required features for Agora Octave (which I've been working on for the past couple of months, as part of the European Space Agency's [Summer of Code 2012](/posts/socis-2012-with-octave/)) is the ability to display syntax-highlighted code. Ideally, the code would come adorned with correctly-aligned line numbers as well (which can be linked to directly), and the code would be wrapped around so that you don't have to scroll horizontally to view the end of long lines.

Here's an example of what it should look like:

![Yay line numbers](/img/posts/line-numbering/line-numbering.png)

My first attempt towards this noble goal was a fairly lackluster one that resulted in a horizontal scrollbar whenever there was one line that was too wide for the box:

![Horizontal scrollbar](/img/posts/line-numbering/line-number-alignment-1.png)

It was pointed out in the mailing list that enabling line-wrapping by default might be better, which I was able to accomplish by simply setting the `white-space` CSS attribute to [`pre-wrap`](http://www.quirksmode.org/css/whitespace.html). Unfortunately, when you add line numbers to the mix, this is what happens:

![Uhoh, line numbers](/img/posts/line-numbering/line-number-alignment-3.png)

One way to fix that is to output the line number within the same element as the contents of the line. Using a table, this involves showing each line within a `<tr>`, with one `<td>` for the line number and one `<td>` for the contents of the line. This is the result:

![Everything is perfect! Or so I thought](/img/posts/line-numbering/line-number-alignment-4.png)

Which, as I [posted about several weeks ago](http://dellsystem.me/posts/agora-octave-update-5-1/), seemed to resolve the problem.

## A wild complication appears

The day after I [pushed the line-number alignment fix](http://inversethought.com/hg/agora-dellsystem/rev/7d753658dc0e), I was informed via IRC that what I thought to be a bulletproof solution actually broke a very important feature: the ability to highlight a code snippet and then copy and paste it elsewhere. See, the fact that the line numbers were now integrated with the code itself meant that when you try to highlight a piece of code, you end up getting the line numbers as well:

![This is not what was meant by syntax highlighting](/img/posts/line-numbering/line-number-highlighting.png "Seeing this made me nauseous")

At first, I panicked, thinking that all my efforts were for nought and that I would never get to live in a world in which Agora had a decent way of displaying code.

Then, I recalled the training I had received at boot camp, from my short stint in the Web Developer Paramilitary Forces: "Don't panic. There is probably some CSS attribute for that. Also, it probably doesn't work in Internet Explorer, but who cares. Does anyone even use that anymore?"

So I stopped panicking and did a search for [css disable selection](https://www.google.ca/search?q=css+disable+selection). The top result was a [StackOverflow post](http://stackoverflow.com/a/4407335) that happened to be exactly what I wanted. Essentially, the trick is to make use of the `user-select` CSS attribute (and all of the vendor-prefixed variations, for the different browsers out there) on the table cells containing the line numbers:

{% highlight css %}
-webkit-touch-callout: none;
-webkit-user-select: none;
-khtml-user-select: none;
-moz-user-select: none;
-ms-user-select: none;
user-select: none;
{% endhighlight %}

Two minutes later, I had [pushed a fix](http://inversethought.com/hg/agora-dellsystem/rev/5f5f838c1e32), and the world was beautiful once more. (In my haste to get out a fix, I made a typo, which was corrected [twenty minutes later](http://inversethought.com/hg/agora-dellsystem/rev/4d5f23285bc2). Not sure why I didn't just copy and paste; StackOverflow doesn't even _have_ line numbers.)

Here's what it looked like after the fix had been applied:

![Proudest moment of my life](/img/posts/line-numbering/line-number-user-select.png "My greatest accomplishment")

If that were the end of it, I would probably have forgotten about the topic entirely and would certainly never have written a blog post about it. By which I mean, that was not the end of it.

## The user-select property is a lie

About three days ago, my SOC mentor Jordi informed me that although line numbers no longer _appeared_ to be selected, they would still show up when you tried to copy and paste a snippet. Once again, my world was shattered. Looking into this more, I discovered that this issue has been [reported](http://code.google.com/p/chromium/issues/detail?id=147490) [as](http://code.google.com/p/chromium/issues/detail?id=70891) [a](https://lists.webkit.org/pipermail/webkit-unassigned/2012-March/417486.html) [bug](https://bugzilla.mozilla.org/show_bug.cgi?id=166235) for Chromium and Firefox (and probably other browsers). In some reports, the issue is said to have been fixed. However, the Mozilla Developer Network [specifications](https://developer.mozilla.org/en-US/docs/CSS/user-select) for the `user-select` property seem to indicate that this is actually intended behaviour:

> Controls the appearance (only) of selection.  This does not have any affect on actual selection operation.

After shedding some tears, I decided I had several options. One was to go back to the original system, with the horizontal scrollbar, which seems to be the most popular way of aligning line numbers (see: [Github](https://gist.github.com/4cfae474ac8a9453a444), [Bitbucket](https://bitbucket.org/snej/murky/src/f7e17ba25f79/Source/unicode/utf_old.h#cl-283)). Another was to simply ignore the fact that users couldn't select text without catching the line number as well, which is what [Trac](http://trac.edgewall.org/demo-1.0/browser/trac.git/ChangeLog?rev=910219766ce6fd0b218a03be76de81afd7a0348b#L1) and the [Mercurial web server](http://inversethought.com/hg/agora-dellsystem/file/d6f65888e0f3/LICENSE) seem to be doing. And then there's [SourceForge](http://sourceforge.net/p/octave/code/11161/tree/trunk/octave-forge/main/comm/src/galois-def.cc#l3 "Try viewing the rest of that line! Oh wait, you can't."), which, I believe, is a strong proponent of the innovative "If the line is too long, then we'll just cut it off, lol" method. [Pastebin.com](http://pastebin.com/CG1PsKhZ) comes the closest I've ever seen to solving this problem, with the line numbers properly aligned and not selected when you highlight the code (even if they appear to be), but they introduce weird whitespace to the beginning of lines and to be honest I have no idea what they're doing.

I ended up going with the other option: making it work. It took a while, and it's not the most elegant one, but it does work. You can view a demo here: <http://agora.dellsystem.me/snippet/8DVW/> (although if it doesn't work for you, I'm starting to think that I'd rather not know).

## The final solution

Although I hate the idea of using Javascript to accomplish what really _should_ be possible without it, it seemed like I had no choice. Line numbers are now inserted via Javascript. The container for the snippet is relatively positioned, and the line numbers are absolutely positioned, with their top offset set to the top offset of the line they are meant to indicate. To see how this is done, check out [the commit](http://inversethought.com/hg/agora-dellsystem/rev/00c71a6192de).

## Other solutions

* Stash, a Git management tool by Atlassian, apparently has a solution for this, which they blogged about [here](http://blogs.atlassian.com/2012/09/stashs-pseudo-line-numbers/). This would have been perfect, except I was not able to reproduce their solution, and since Stash is one of those products that require you to buy a license first I wasn't able to test it out, either. (They do ostensibly have a ["try it for free" option](http://www.atlassian.com/software/stash/download), but that page seemed broken when I looked at it.) If I do manage to get that working, it will almost certainly render my Javascript technique obsolete. But hey, progress is good.
* Sourceforge, despite its flaws, actually has a pretty clever of handling linking to a specific line. Click on any line and you'll jump to that anchor. This opens the door to a different solution: if the line numbers don't need to be clickable, they could be hidden (in terms of `z-index`) behind the lines themselves, which _might_ prevent them from being selected. I tested this out a bit, and though I wasn't able to get it working, it remains a possibility. Sourceforge's implementation of this requires Javascript, which makes it hardly any better than mine, but it could probably be reworked to function without it.
* **Update**: It turns out Pastebin uses an ordered list to display the numbers. That is actually extremely clever and even sort of semantic. I don't know why I didn't realise this earlier. The only problem with this solution is that when you highlight the text, the line numbers _appear_ to be in the selection, even though they don't show up when you copy and paste it anywhere. Even `user-select` can't handle this. There might be another way, but for now, I'm going to give this method a pass.

## Closing remarks

Was this worth it? Well, maybe. I learned some things about CSS (and, in the process, myself!!11). In any case, it's not like I had a better way to spend my Friday night. Unfortunately, this does mean that I wasn't able to finish the features for Agora that I promised [last week](/posts/agora-octave-update-7/). Expect an update on that in the next few days.

My hope is that someone, someday, who happens to be looking at an Octave snippet on Agora, will notice my painstakingly crafted solution to the hardest problem in computer science. And, instead of thinking, "Wow, I can't believe someone went to the trouble of making this combination of features work together, that's such a pointless thing to do", this person will instead think, "Wow, what a brilliant solution to an otherwise intractable problem. This web developer is clearly a genius, and we should give her a job."

At the very least, I should be able to get a paper out of this. I'm thinking Nature.
