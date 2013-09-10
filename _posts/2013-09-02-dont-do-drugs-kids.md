---
layout: post
title: "How not to check the validity of an email address"
categories:
- security
- mcgill
- desire2learnhow2code
image: email
code: true
---

_Another update, after this post somehow hit #1 on Hacker News and garnered my
website more visitors in one hour than it usually gets in a year: I got a lot of
feedback on this post. While a lot of it was positive, there was also some valid
criticism about the amount of flaming in this post. While at first my response
was along the lines of "h8rs gunna h8 lol", after some thought I realised that
while posts like this can be fun to write, they can also be counterproductive
and even harmful to the developer community. I know that if someone had found
some of my code and decided to publicly rip it apart, I would almost certainly
feel hurt — even if it were deserved (like [that time I wrote a custom CMS and
made it vulnerable to SQL
injection](https://github.com/dellsystem/ssuns-2011/pull/14))._

_I was young and foolish when I wrote this post. Admittedly, I'm less than a
week older now, but hopefully much less foolish. Although I don't regret writing
this post, I don't think I will be making posts of a similar nature in the
future. While I do believe that bad practices in the developer community should
be called out, there are undoubtedly ways of getting the same message across
without resorting to vitriol or an overly snarky tone — even if the end result
runs the risk of being less entertaining. Posts like this have a tendency to
exacerbate a culture that is already mired in toxicity, and while recognising
this fact cannot completely absolve me, I hope that it will at least deter
others from behaving similarly._

_I considered taking this post down, but that seemed silly considering that 99%
of people who will ever read this post have, in all likelihood, already read it.
In addition, I am no longer afraid of being sued for defamation by the vendor,
since they seem to have taken it in stride and — amazingly enough — have even
expressed an interest in interviewing me for a developer position as a result of
this blog post. If the original programmer ever reads this post, I apologise for
the public ridicule at your expense. All I can say is that I hope you no longer
write code like this. Though if you do, please send it to me and I will do my
utmost to write a sincere, snark-free analysis of it. <3_

_As a sidenote, one thing I found rather surprising is the fact that a
significant number of readers seemed to interpret this post as an ode to my
hatred of drugs. This would have been ideal if I ever intended to run for
office, but since I don't, it's just perplexing; I would have thought the tone
of the post made it obvious enough, but since it clearly wasn't, I will clarify
that I merely took an over-the-top approach and ran with it, in the interest of
writing an article that would be more interesting to read than "Here's some code
I found". It is a fairly lazy literary technique, though, and probably not one I
will be using again anytime soon. (Hey, I never claimed this post was a literary
masterpiece. I promise it will get better, though.)_

***

Pretend, for a moment, that you're a newly hired programmer working on a popular
learning management system called Hot4Learning. Your predecessor had been
working on adding email functionality to the system, so that any user would be
able to send an email to any other user at the school via a web interface.
Unfortunately, your predecessor was recently hit by a bus and never managed to
complete his magnum opus. Your task is to finish it by adding an email
validation feature, to ensure that an email is sent only if the recipient is a
valid email address associated with the school.

For example: if Bob is a student at McGill University, then he should be able to
send an email to any valid @mail.mcgill.ca or @mcgill.ca email address. So if
his friend Jane's school email is jane.smith@mail.mcgill.ca, then Bob should be
able to send an email to that address. On the other hand, he should not be able
to send an email to jane.smith@gmail.com. Nor should he be able to send an email
to thisisnotavalidemail@mail.mcgill.ca.

So your job is to write this feature, assuming you have access to a list of
valid emails for the school.

I hope you're thinking, "Please, that's easy. First, I'll create a string by
joining the emails in the list with the string `'|****|'`, then I'll pass that
to the client by assigning the string to a variable within a `<script>` tag.
Next, in the Javascript, I'll instantiate an `Array` object and assign it to a
variable endearingly named `temp`, then throw away the aforementioned Array
object and set temp to be the array created by splitting the string on
`'|****|'`. Whenever a user enters an email, I'll convert it to lowercase and
store it in a variable with the beguiling name `curForwardUserName`, and I'll
create a variable called `validUserName` which I will set to be the string
`'0'`, because why use a boolean when you can use a string? Then, I'll loop
through the entirety of `temp`; for each email address in `temp`, I'll convert
that to lowercase, then check if it's equal to `curForwardUserName`. If so, I'll
set `validUserName` to the string `'1'`, and break. Finally, if `validUserName`
equals the string '`1`', I'll consider `curForwardUserName` to be a valid email
address; otherwise, it's invalid.

Actually, no. That's a lie. I really hope that's not what you're thinking. I
hope what you actually thought was along the lines of "Well, obviously I'd do
the validation on the server side. I can store the valid emails in a data
structure that allows O(1) membership testing, then check if the input email is
contained in there." Because, well, that's the right way to do it.

## This is your brain

In Python, the right way to do it would look something like this:

{% highlight python %} if input_email in valid_emails_set:
send_email(input_email, another_param, etc) {% endhighlight %}

## This is your brain on drugs

On the other hand, if you're working on a product called Hot4Learning, you
probably hate your job and need to consume a staggering amount of drugs in order
to keep coming to work. This is what your drug-addled brain might come up with:

_Warning: NSFWUYWOH (Not Safe For Work Unless You Work On Hot4Learning)_

{% highlight html %} <script>
// [some other code here]
var userNamesStr =
'a.fakelastname@mail.mcgill.ca|****|another.fakelastname@mail.mcgill.ca
|****|(pretend there are 70,000 more emails
here)|****|zamboni.man@mail.mcgill.ca'; var temp = new Array(); temp =
userNamesStr.split('|****|'); var validUserName = '0';
// [more code here]
for( i =0; i< temp.length; i++){ if( curForwardUserName == temp[i].toLowerCase()
) { validUserName = '1'; break; }
// [some last bits of wisdom before we go]
</script> {% endhighlight %}

_UPDATE: Yes, the above code does involve sending all 70,000+ McGill email
addresses to the client upon each page load. The source code of the page was
over 2.5MB in size. As in, 2.5MB of pure text._

Since your reviewer would likely be as stoned as you, you would get a quick LGTM
and the above code would soon find its way into production.

## The actual story

Last year, the IT department at McGill University replaced the old LMS
(Blackboard) with a new system (which is not actually called Hot4Learning, but
the actual moniker is no less trite or gimmicky so I'll spare you). Since the
old system was riddled with vulnerabilities and suffered from general all-around
shittiness, I was excited to see what the new system would be like. That
excitement soon died, just like brain cells do when exposed to copious amounts
of drugs.

Upon clicking the "email" tab, I was greeted with 10 seconds of white screen as
my browser tried to load the page. "Why on Earth is this taking so long?" I
asked myself. "It can't be, like, trying to load every single valid email
address at McGill, right? Lol. Haha. Hahaha. Hahahaha. Wait. ohgod"

Words cannot express the horror I felt when I looked at the source of the page
and found the code that I have reproduced above. The only time I've been more
terrified was when I dreamt that I slept through my cryptography exam and then
began to suffocate (but that turned out to just be the blanket).

If you want to take a look at this code in the wild, well, you can't anymore. I
reported it as a data leak vulnerability and the vendor actually fixed it within
two weeks. However, the code as it appeared then is essentially what you see
above, shitty whitespace and all; I just removed some code irrelevant to the
functionality at hand and also removed the actual list of emails. Apologies to
Zamboni Man if you exist and are a student at McGill.

I would really like to know the combination and quantities of drugs consumed
that resulted in this code. Do you know? Can you hook me up? Send me a message
on Twitter [@dellsystem](https://twitter.com/dellsystem).

## Legal addendum

I hereby claim that the above snippet of code is fair dealing according to
section 29 of the Copyright Act of Canada, which allows for usage for the
purpose of research, private study, education, parody, satire, criticism or
review and news reporting. In fact, this snippet was used for nearly _all_ of
these purposes:

### Research

I stumbled upon this snippet while doing research for my B.S. thesis, "Not even
once: Prolonged drug use and its effect on code quality". It will be the perfect
B.S. thesis, complete with B.S. graphs and footnotes in which I beg the reader
to take me on as a grad student.

### Private study

I saved the source code of the page because I wanted to privately study the
correlation between prolonged drug use and code quality.

### Education

I would like to educate the public on the deleterious effects of prolonged drug
use on code quality.

### Parody

I wish I could say that the code above is a parody of the actual source code I
encountered. I really do. But I can't.

### Satire

The code above was used as part of a scathing satirical indictment of the modern
programmer's tragic penchant for drugs. Also, society.

### Criticism or review

3/10 would not bang

### News reporting

BREAKING: Prolonged drug usage can result in terrible code. CNN had better link
back to me when they pick up this story, I could use the ad revenue.
