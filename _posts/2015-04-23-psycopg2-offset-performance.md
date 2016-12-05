---
layout: post
title: psycopg2 OFFSET performance with large tables
code: true
categories:
- postgresql
- python
---

_This post is about solving a minor performance issue that can be encountered
when using [psycopg2][psycopg], a commonly-used Python driver for PostgreSQL. It will
likely be of zero interest to you unless you have come across this problem
before. Even then, it is doubtful that it is worth reading all the way through
unless you have this problem *right now* and don't mind wading through
excessively flowery language and unnecessary metaphors to find the solution.
Don't say I didn't warn you._

If you've ever tried to go through the rows of a table sequentially using a
combination of OFFSET, LIMIT, and a loop structure of some sort, you may have
discovered that while everything was all fine and dandy for the first few
thousand rows, it all starts to go downhill at some point. Or downtable, as it
were. Well, to be specific, it's _supposed_ to be going downtable, and it
does, but each subsequent iteration of the loop takes longer than the previous
one, and you fear that you'll never reach endtable.

I had this exact problem recently. Like most problems encountered by
programmers these days, it has been asked and subsequently answered on
[StackOverflow][stackoverflow]. The answer was enough to point
me in the right direction, but wasn't especially detailed, so I thought I'd
write up a little guide in case anyone else has the same problem that I had.

The gist of it is that you need to use a [named cursor][named-cursors] and call
`cursor.fetchmany(n)` each time you want to fetch `n` rows (or
`cursor.fetchone()` to fetch one row at a time). That's really all you need to
know to solve this problem, to be honest. If you're curious about how I managed
to write another 681 words on this topic, read on for the exciting details of
my adventures with psycopg2.

## How to improve OFFSET performance: a step-by-step guide

**Step 1:** Use PostgreSQL for storing some of your application's data.

**Step 2:** Discover that one of your tables has hundreds of millions of rows.
This is not due to any errors or flaws in the design of your application;
that's just how much data there is. Contemplate, briefly, the insignificance of
your own existence in the face of this metaphorical mountain of data. Realise
that many brave men and women have conquered mountains much, much larger than
this, and that you have a long way to go before you can call this mountain "big
data", or even "mildly large data".

**Step 3:** Write a Python script, to be run in the background, that will go
through the rows in the aforementioned table and do various things with them,
in batches of 100. Since you've downplayed the size of the metaphorical
mountain in your head and, in fact, think of it as "fairly small data", you
will completely disregard any performance-related concerns, and will instead
use the most basic SQL techniques you can think of for doing this sort of
thing with psycopg2:

{% highlight python %}
query = """SELECT thing FROM things LIMIT %s OFFSET %s;"""
limit = 100
offset = 0

while True:
    offset += limit
    cursor = db.cursor()
    cursor.execute(query, (limit, offset))
    record = cursor.fetchall()
    if record:
        yield [r[0] for r in record]
    else:
        return
{% endhighlight %}

**Step 4:** Set up supervisor to run your script and start it. Because the
various things that must be done to each batch of 100 rows are a touch on the
slow side, and because you have better things to do than watch the output of
`tail -f` all day long, you will fail to notice any performance degradation at
all for several weeks.

**Step 5:** Somewhere in the vicinity of the one millionth row, you begin to
notice that, hey, the script is taking a lot longer than it should. Suspect
that running multiple queries, each with an OFFSET of potentially millions of
rows, is not going to be instantaneous. Remember that each such query requires
a sequential scan on the table, and that each subsequent scan will take longer
than the previous one.

**Step 6:** Try various Google queries with some combination of the words
"psycopg2", "postgres", "offset", and "performance" in the hopes of finding a
good alternative to your current implementation. Surprise yourself by finding
the answer to almost your exact question on [StackOverflow][stackoverflow].

**Step 6**: Rewrite your code using one named cursor (as opposed to potentially
millions of unnamed cursors, none of which will be allowed more than a
tragically brief existence) to create a server-side cursor:

{% highlight python %}
cursor = db.cursor(name='things')
cursor.itersize = 100
query = """SELECT thing FROM things;"""
cursor.execute(query)

while True:
    record = cursor.fetchmany(cursor.itersize)
    if record:
        yield [r[0] for r in record]
    else:
        cursor.close()

        return
{% endhighlight %}

**Step 7:** Commit your changes with a message that is both jubilant (at having
fixed this performance issue) and sheepish (at having allowed the performance
issue in the first place). Restart the script and amuse yourself for a few
minutes by watching its progress.

**Step 8 (optional):** After a few days of nonstop SELECTING of thing FROM
things, check disk space usage on the machine on which Postgres is running.
Panic upon realising that you are, against all probability, using 100% of the
available disk space. Discover that creating a server-side cursor prevents
vacuum operations from occurring during the lifetime of the cursor. Resign
yourself to periodically stopping and restarting the script to allow vacuuming
to occur. _Note that this step is completely avoidable if 1) the script stops
running after a reasonable amount of time; or 2) you have a large disk relative
to the amount of data you're producing. This step is not avoidable if the
script is expected to run more or less constantly and you produce enough data
to overwhelm your disk after a few days when vacuuming is disabled. May
you have better luck than I._

[stackoverflow]: http://stackoverflow.com/a/7976113
[psycopg]: http://initd.org/psycopg/docs/usage.html
[named-cursors]: http://initd.org/psycopg/docs/usage.html#server-side-cursors
