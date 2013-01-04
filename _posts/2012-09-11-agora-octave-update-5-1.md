---
layout: post
title: "Agora Octave: Update #5.1"
categories:
- agora
- django
image: socis-2012-with-octave
code: true
---

This is the follow-up to [update #5](/posts/agora-octave-update-5/) (a little bit later than planned). Summary of changes this week: updating the [code page](http://agora.dellsystem.me/code) to make it slightly more useful (at least in terms of listing the snippets), fixing vertical alignment of lines and their corresponding numbers on the snippet view page (more on that [below](#line-number-alignment)), and adding a pop-up window for a more streamlined login and registration process.

## This week

### Updates to the code page

This is nothing major, I just changed the layout slightly (the buttons have been moved), changed some of the terminology (bundles/singles are now known collectively as "modules", for now), and added the list of the 5 most recent snippets, as well as some placeholder text for forge and module sections. [View demo &raquo;](http://agora.dellsystem.me/code)

<a name="line-number-alignment"></a>

### Line number alignment

This one might require a bit of background. Previously, the line numbers were being output in a separate loop from the actual lines themselves, within one giant `<pre>` tag nested within a `<th>`. The problem with this method is that if a line is ever too wide for the box, then it gets hidden and you have to scroll horizontally to see it, as in the following screenshot:

![Screenshot of snippet with orizontal scroll](http://cs.mcgill.ca/~wliu65/media/agora/line-number-alignment-1.png)

This method worked for me, because I have a touch pad with horizontal scroll enabled, so I didn't think much of it. However, it was brought up on the [mailing list](http://octave.1599824.n4.nabble.com/Agora-updated-td4643920.html) that this can be inconvenient for users who don't have a way to easily horizontally scroll, so I decided to look into it again. Although there existed a "toggle wordwrap" link, which users could click to toggle the line-wrapping of the snippet (and so eliminate the need to scroll horizontally), that feature also caused the line numbers to disappear:

![Screenshot of word wrap with no line numbers](http://cs.mcgill.ca/~wliu65/media/agora/line-number-alignment-2.png)

I had to do it this way because any line that is wider than the box itself would, when wrapped, push down the content after it, without affecting the placement of the line numbers as well. In other words, you would end up with something like this:

![Screenshot of word wrap with incorrect line numbers](http://cs.mcgill.ca/~wliu65/media/agora/line-number-alignment-3.png)

The line numbering here is just plain wrong. In the end, I simply changed the way line numbers and lines are outputted by using a single loop and a `<tr>` for each line, and now it looks much better (with word-wrapping used by default):

![Screenshot of word wrap with correct line numbers](http://cs.mcgill.ca/~wliu65/media/agora/line-number-alignment-4.png)

The only thing that was difficult was getting the styling to match how it looked before, as the change in the HTML structure made it a bit tricky. It should be pretty much the same now, although the corners look a bit off with a dark background.

### Streamlined login and registration

We now have a slightly more streamlined login/registration system: simply click any login or registration link and a window should pop up asking you to fill out the combined login/registration form. If you are successfully logged in, you will be returned to the page you were previously looking at. For a demo, click the "Login or register" link at the top right of the [code page](http://agora.dellsystem.me/code). (Please don't actually register because the registration app sends out an activation email by default, and email isn't enabled on my server so it just won't work. To test logging in, use the username `test` and the password `test`.)

## Next week

(Technically, this week. Next blog post will be on Friday, September 14.)

### Module upload

I've started working on an app for handling module uploads. It will be similar to snippets in the way that it is structured, but it will be more powerful in that users will be able to upload files rather than being limited to copying and pasting (either a single file in plain text, or an archive containing multiple files). I will try to get the bulk of this done by my next update.

### Profiles

I will continue working on user profiles: layout, features (including the ability to change your default syntax highlighting colour scheme, as mentioned in a previous update), and editing your own profile.

## Position in timeline

* _**August 1-15:** Check out codebase, get it running; read all the code and documentation; start learning Mercurial_
* _**August 16-31:** Start working on design; start mocking up models and routes for the components_
* **September 1 - October 15: Work on the core components, with as much test coverage and documentation as is feasible; start implementing the views, models and templates**
* _**October 16-31:** Ensure that documentation is thorough and up to date; write any remaining tests that need to be written; test out the user interface and fix any bugs_
