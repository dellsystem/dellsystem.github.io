---
layout: post
title: Predicting the U.S. election without polls
categories: endorsementdb
---

A few days after the United States presidential election, [Data Driven
Journalism] featured a great piece about the pitfalls of relying on opinion
polls to predict elections: ["Will data driven election reporting ever be the
same?"][ddj] I myself had fallen into the trap of trusting the polls that
predicted a landslide Clinton win, so in the aftermath of the unexpected
election results, I started thinking about alternatives to traditional polls
for predicting election results. Endorsements, perhaps. Maybe if you looked at
the number of endorsements by politicians in a particular state, you'd be able
to predict the outcome in that state.

Luckily, I happened to have that data on hand.

## [EndorsementDB.com]

In the weeks leading up to the election, I built [EndorsementDB.com], a
database for tracking public endorsements (and un-endorsements) of presidential
candidates by notable figures. The goal was to store endorsement metadata in a
structured but flexible way, allowing for arbitrary tags and thus
facilitating open-ended queries. I started by manually adding endorsements
as I encountered them in the news, tweaking the schema as necessary to
accommodate increasingly complex types of endorsements: "LeBron James endorses
Hillary"; "The Chicago Tribune endorses Gary Johnson"; "Republicans Endorse,
Unendorse And Then Re-Endorse Donald Trump".

Although I managed to import several hundred endorsements manually, I soon
realised that I had severely underestimated the sheer volume of endorsements --
over 8000 in total -- that had accumulated throughout the campaign season.  So
I changed my strategy: I would add endorsements by parsing the relevant
Wikipedia pages and importing them programmatically, with manual supervision
as needed. That dramatically sped up the process, allowing me to import
all the endorsements from the relevant Wikipedia pages. Once those were
imported, I programmatically tagged what I could based on the context on the
Wikipedia pages, and then manually added in some other tags that I thought
could be relevant (for example, all the members of Congress, complete with
their party affiliation and state).

## Endorsements among members of Congress

Now, going back to the original premise: How could we have predicted the
outcome of the election without using polls? Well, given that we have a
database of the endorsements made by all the members of Congress, we can start
there and see how these endorsements align with the popular vote in each state.

As a side note: since this analysis is being done after the election is over,
the goal of this analysis is not to try and dazzle you with my clairvoyance.
(The design of these models was indisputably tainted by my knowledge of
the actual election results, with the risk of overfitting and confirmation
bias that entails.) Rather, the aim of this post is to explore the correlation
between endorsements and election results -- a correlation that I'm sure many
would suspect, but might find difficult to quantify. To that end, I tried to
keep the models straightforward and reasonable, with clear explanations of how
I produced each of them.

For simplicity, these models all treat Nebraska and Maine as winner-take-all
states even though they actually use a [district-based
model](http://www.270towin.com/content/split-electoral-votes-maine-and-nebraska).

### Party affiliation as a baseline

We start by ignoring endorsements and only looking at party affiliation as a
baseline model. For each state, we look at the party breakdown of its members
of Congress, and award that state to Trump if most members are Republican, and
to Clinton if most are Democrat. If there is an equal number from each party,
we treat the prediction as a tie; if the winning party has only a small edge
percentage-wise, we predict a smaller margin of victory.

The results are shown in the table below. Clinton victories are shown in blue,
and Trump victories are shown in red, with a white background to indicate a
small margin of victory (under 5%). The numbers after the first row of the
"Predicted electoral votes" column indicate the difference between the two
parties, with the actual number of electoral votes awarded to each state shown
in the first column.

<img src="/img/posts/predicting-elections/congress-party-model.png" alt="" />
<p class="caption">
    A table with the outcome of the "Congress - party" model highlighted,
    alongside models that use only members of the Senate or House, which were
    excluded from this analysis for the sake of brevity. Only the states that
    were predicted incorrectly are shown. You can view the full table at <a
    href="http://endorsementdb.com/stats/predictions#category-1">
    endorsementdb.com</a>.
</p>

This model, which projects a landslide Trump victory of 337 to 197 electoral
votes, performs decently well: of the 50 states and D.C., only 5 predictions
are wrong, and they all happen to be the states that were won narrowly, with
less than 5% spread (Colorado, Maine, Nevada, New Hampshire, Virginia).

Of course, the problem with looking solely at party affiliation is that it
produces a very limited model: it implies that control of Congress will lead
to winning the election, which we know isn't always the case. Plus, it implies
that sitting members of Congress -- some of whom were elected six years ago --
are, for whatever reason, an accurate representation of voting preferences
today. What's more, we know that people don't always vote along party lines, a
fact that is especially relevant for this election, as many Republicans decided
not to endorse their Party's nominee.

### Using endorsements instead

Bearing that in mind, we turn our attention instead to endorsements. For this
model, we award a state to the candidate with the most endorsements among
members of Congress. For simplicity, we ignore declarations of support that are
explicitly stated to not be endorsements (a queer phenomenon that appears to be
specific to Trump; you can see a list of such endorsements at
[endorsementdb.com][trump-support]), as well as those of
the form ["I would support the Republican ticket if Trump were to withdraw and
be replaced by Pence"][pence]. (It would be interesting to account for these
pseudo-endorsements in another analysis, however.)

<img src="/img/posts/predicting-elections/congress-endorsement-model.png" alt="" />
<p class="caption">
    A table with the outcome of the "Congress - endorsement" model highlighted,
    alongside models that use only members of the Senate or House, which were
    excluded from this analysis for the sake of brevity. Only the states that
    were predicted incorrectly are shown. You can view the full table at <a
    href="http://endorsementdb.com/stats/predictions#category-2">
    endorsementdb.com</a>.
</p>

This time, only three predictions were wrong: Michigan (a tie), Virginia (small
Trump margin), and Wisconsin (a tie). The result is still a Trump victory --
even ignoring Wisconsin and Michigan -- but with a smaller margin: 292 to 220.

This model is more reasonable in its implications -- namely, that the feelings
of members of Congress towards the presidential candidates can influence, or
otherwise reflect, the feelings of their constituents -- and the predictions
are a definite improvement over the baseline model. However, the presence of
ties is suboptimal, since we wouldn't expect any ties in the actual vote
counts. Furthermore, this model treats members of the Senate and the House
equally, even though each state has only two members of the Senate (who are,
typically, elected every six years) but up to 53 members of the House (who are
elected every two years). If we want better precision, we'll have to find a
reasonable way of breaking those ties, taking this difference into account.

### Breaking ties

To that end, I came up with three ways of breaking ties. All of these models
made exactly one false prediction, and correctly predicted the popular vote spread
(whether it's less than or greater than 5%) for at least 41 of the 51
states/districts. Two of the models incorrectly predict Virginia for Trump; the
other model predicts Michigan for Clinton (due to both sitting Senators being
Democrat).

Note that all three models predict a comfortable Trump victory.

<img src="/img/posts/predicting-elections/tiebreaker-models.png" alt="" />
<p class="caption">
    A table with the outcome of all three "tiebreaker" models. Only the states that
    were predicted incorrectly by any of the models are shown. You can view the
    full table at <a
    href="http://endorsementdb.com/stats/predictions#category-3">
    endorsementdb.com</a>.
</p>

## Lessons learned

If I had done this analysis before the election, I certainly would have been
less quick to believe that Clinton would have won in a landslide, as many polls predicted.

Of course, I say this with the privilege of hindsight. If she _had_ won, would
I still have performed this analysis afterward? Would I have discarded the
results when they indicated a Trump victory? Maybe; I don't know. At the same
time, it may be that these endorsements form an important bellwether for the
election results, meaning that Clinton wouldn't have had a chance unless more
Republicans in Congress had decided to endorse her over third-party candidates
like [Evan McMullin] and [Gary Johnson] or [a Republican other than the
nominee][another-republican].

Incidentally, I also learned that newspaper endorsements were not a great
predictor of the outcome of this election. This would be obvious to
anyone who is aware that the vast majority of newspaper endorsements were for
Clinton, with only a handful for Trump. If you focus on the number of local
newspapers endorsements by state, you'll find that Clinton is projected to win
every single state except Alaska and Kansas, which is pretty hard to imagine.
Even if we change the model to only award a state to Clinton if Trump gets _no_
newspaper endorsements -- which, to be honest, is a pretty contrived rule -- we
still get 20 mispredictions. Clearly, newspaper endorsements were not a great
predictor of how voters felt during this election. Why that was the case is
anyone's guess.

<img src="/img/posts/predicting-elections/newspaper-models.png" alt="" />
<p class="caption">
    A table with the outcome of both newspaper endorsement models. The data
    comes from the <a
    href="https://en.wikipedia.org/wiki/Newspaper_endorsements_in_the_United_States_presidential_election,_2016">"Newspaper endorsements in the United States presidential election, 2016" Wikipedia page</a>.
    You can view the full table at <a
    href="http://endorsementdb.com/stats/predictions#category-3">
    endorsementdb.com</a>.
</p>

### Caveats

While I believe these methods would be a useful part of a pollster's arsenal
for future elections, I do acknowledge some caveats. Given that we have only
one event - the 2016 election - to draw from, there is a real risk of
overfitting in these results. All I've shown is that for the 2016 election,
there is a correlation between presidential endorsements by members of Congress
and the popular vote in each state, which is slightly stronger than that
between their party affiliation and the popular vote. It's possible that is
only true because of the unique circumstances of this election year: Congress
was overwhelmingly under Republican control, and the Republican nominee was a
uniquely polarising figure who, throughout the course of his campaign, lost the
endorsement of many Republican members of Congress. It would be interesting to
apply these models to previous elections to see how they hold up, but
unfortunately historical endorsement data is more challenging to obtain,
especially pre-2008.

It's also unclear why, exactly, this correlation exists. Do members of Congress
make their decisions based on who they think their electorate would support?
Do voters change their mind based on who their representatives support? Is
there something else -- something geographical, or cultural -- that just
happens to align these two populations most of the time? Is it some combination
of all three? On this, I can only speculate.

Still, the fact that even the most basic endorsement-based models did decent
job of predicting the election speaks to the importance of endorsements.  I
personally think that such endorsements should be tracked, for accountability
purposes (especially when it comes to public officials) and because of their
potential as a barometer for public opinion (partly because these people often
have influence, and partly because it can indicate the sentiment among their
audience). Endorsements are often overlooked in statistical analysis because
of the difficulty of obtaining the necessary data, which is why I will continue
to work on [EndorsementDB.com] with the goal of making it a central source of
endorsement data for this and future elections.

You can view the entirety of the tables included in this post at
<http://endorsementdb.com/stats/predictions>, or browse the 8000+ endorsements
at [EndorsementDB.com]. The source is on GitHub (along with the data, which I
really shouldn't be storing in Git given the size of the files) at
<https://github.com/endorsementdb/endorsementdb.com>.

If you find this interesting and want to get involved in any way, please
reach out by [email](mailto:admin@endorsementdb.com) or [Twitter]! I'd love to
hear your thoughts or help you with a research question that involves
endorsement data. I have some more research questions of my own -- like the
effects of presidential endorsements on Senate and House races -- and I'll be
writing up a post if I find anything interesting, so stay tuned.

_This post was featured on Data Driven Journalism as ["EndorsementDB:
Predicting the U.S. election without polls"][ddj2]._

[ddj]: http://datadrivenjournalism.net/news_and_analysis/will_data_driven_election_reporting_ever_be_the_same
[ddj2]: http://datadrivenjournalism.net/featured_projects/endorsementdb_predicting_the_u.s._election_without_polls
[EndorsementDB.com]: http://endorsementdb.com
[trump-support]: https://endorsementdb.com/#candidate=trump-support
[pence]: https://endorsementdb.com/#candidate=pence
[Evan McMullin]: http://endorsementdb.com/#form=eyJzb3J0Ijp7ImJ5IjoiZm9sbG93ZXJzIiwidmFsdWUiOiJtb3N0In0sImZpbHRlciI6eyJ0YWdzIjpbMTMsMTJdLCJtb2RlIjoicGVyc29uYWwiLCJjYW5kaWRhdGUiOiJtY211bGxpbiJ9fQ
[Gary Johnson]: http://endorsementdb.com/#form=eyJzb3J0Ijp7ImJ5IjoiZm9sbG93ZXJzIiwidmFsdWUiOiJtb3N0In0sImZpbHRlciI6eyJ0YWdzIjpbMTMsMTddLCJtb2RlIjoicGVyc29uYWwiLCJjYW5kaWRhdGUiOiJqb2huc29uIn19
[another-republican]: https://endorsementdb.com/#candidate=another-republican
[Twitter]: https://twitter.com/endorsementdb
[Data Driven Journalism]: http://datadrivenjournalism.net
