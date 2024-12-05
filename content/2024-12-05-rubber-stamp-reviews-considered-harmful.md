Title: Rubber-stamp reviews, considered harmful
Date: 2024-12-05 12:00
Summary: Some thoughts on why we should take the time to make our pull requests easy to review, and how to do so.

For most of us, it's a familiar feeling: one of our teammates has asked us to
review some code. We sit down and start working through the diff... there are
hundreds of lines of changes. Some of it seems sensible, but it's really hard
to follow what's going on from the diff. This is taking ages, and we're already
behind on a bunch of stuff. There's nothing obviously wrong, the tests pass,
and the author's one of the senior developers on the team. I'm sure they know
what they're doing: let's just approve the review.

This is very natural, and I'm sure we've all done it, but if we start giving
these "rubber-stamp" reviews where we approve the changes without really
understanding them, then it's hard to see what the point of doing a review in
the first place was. Code review is great for many reasons — shared
understanding of code, catching edge-cases that the author hadn't thought of —
but you only get those benefits if the reviewer actually understands the
change, rather than just looking for typos and style-guide violations.

So, what should we do? Just review harder? However long it takes, take the time
to understand that pull request? That's not an approach that works well:
ultimately you're redoing a lot of the author's work. There are better
solutions.

## Talk it over

At this point, a lot of people will recommend "get on a call, and get the author to
explain it to you". It's good advice, and can certainly help you as a reviewer
get a grip on the changes and their context.

Personally speaking, I don't find this approach works well for me: I need the
space and time to go and explore the change at my own pace. I catch myself
feeling guilty about using up too much of the author's time while I
think about the thing they just said; alternatively I start simply nodding
along with them, taking us back to rubber-stamp reviews.

Furthermore, while a call is great for rapidly transferring information, it
doesn't help us in six months' time when we need to look at this code
again. Perhaps we discover a bug, or just need to build on top of the
changes. How did all this stuff work again? Why did we do it this way rather
than another? Was it deliberate or an accident?

I'm certainly not going to discourage synchronous communication if it works
well for you, but it's not the full solution for me.

## Make it easy to review

Let's look at this from the other side: that of the author. When I'm working on
a change, I want that change to land quickly and efficiently, so that people
can start using it and I can move on to the next change. I need to make sure it
doesn't sit waiting for review for days or weeks. And one of the best ways to
do this as an author is to *make the review easy*.

If we can set our changes out in such a way that a reviewer can look at it and
say "yes, this is obviously right", then everybody wins. I'm happy because my
code has landed. The reviewer is happy because they didn't have to
reverse-engineer my code. Future maintainers are happy, because if it makes
sense now, it will probably make sense in the future.

The key point here is that, as an author, I have the context around the change:
I know what I am trying to achieve, and why I took the approach I did. The
reviewer might be able to figure it out, but why are we making life difficult
for them?

Here are a few ideas on how to make it easier for a reviewer to understand your
changes.

### Put yourself in the reviewer's shoes

This is general guidance that might be somewhat obvious, but I think it's worth
calling out explicitly, because I frequently see people forgetting to do it
(myself included).

When you're putting some changes up for review, have a think about how it is
going to look to the reviewer. If *you* were looking at this code for the first
time, would you understand it? What questions would you, as a reviewer, want to
ask? What would you wish the author had done to make it easy for you?

### Keep PRs small

Small pull requests are inherently easier to review. They also make it less
likely that a given pull-request will end up with multiple rounds of review;
and if you do end up with multiple rounds of review, it's less mental load for the
author and reviewer to get back up to speed for each round.

With that in mind, try to avoid changing lots of different things in one pull
request. For example, if you've fixed two different bugs, consider whether each
fix could be in its own pull request. Avoid fixing bugs and adding new features
in the same pull request.

Protip: if you aren't familiar with `git rebase --update-refs`, have a read of
[this
article](https://andrewlock.net/working-with-stacked-branches-in-git-is-easier-with-update-refs/). I
find `--update-refs` very useful when I have multiple pull requests in flight at a time.

### Explain what your PR is for

Make sure the pull request contains a description of what it is doing, and
why. Is it fixing a bug? If so, link to the bug report. Adding a new feature?
Explain what the new feature looks like.

This sort of context is obvious to the author, but a reviewer (or someone else
trying to follow the changes, or anyone looking back at the changes in future)
won't necessarily know. Making them reverse-engineer this information is a
waste of time.

### Write some comments on the diff

Sometimes, it can be helpful to write some of your own comments on the changed
lines before asking a reviewer to look at it. This can be particularly valuable
when there are several commits (see
[below](#break-the-pr-down-into-small-changes)) in the pull request and you
want to give the reviewer a bit of context from a later commit.

Don't overuse this though: explanations about how code works or why a
particular approach was taken are normally better left in a *permanent* record
as `/* ... */`-style code comments.

### Break the PR down into small changes

This is probably the most powerful weapon in the "make a pull request easy to
review" armoury, though also the most work for the author.

One of the problems for a reviewer is that, typically, a diff doesn't present
the changes in a logical order. For example, if I'm trying to review code, I
might want to start with high-level changes, and then work my way down the call
stack. Or I might prefer to start at the bottom and work up the stack. What I
definitely *don't* want is to start somewhere in the middle, and then have
changes to high-level functions and low-level functions all mixed in together.

A good way to deal with this is to structure a pull request as a series of coherent
commits. This guides the reviewer to a logical way to read through the
changes. Ultimately, it's much easier to review five 50-line changes than one
250-line change.

For this to work well, the reviewer needs to be able to look at each commit and
see that it is correct: each commit needs to make some sort of sense in its own
right. There might temporarily be "dead" code, but ideally tests should pass
after each commit. In other words: each commit should be "atomic".

Often, I find myself implementing a new feature, and once I've got everything
working, breaking the large change up into new commits. Doing so typically
requires familiarity with relevant `git` commands such as `git rebase`, `git
reset`, and `git commit --fixup`.

Breaking up a large change into smaller commits is not always easy, but it's a
skill worth practicing.

## But I don't have time for all that nonsense!

Look, the code works. The customer needed the feature last week. I've got
another 150 things to deliver for tomorrow. Why are you making me jump through
all these pointless hoops? Don't you trust me? It seems like fixing anything in
this project takes a month.

I certainly understand this frustration. I've felt that way often enough
myself. I think there are a couple of answers, though.

The first is simply that reviewing code is (presumably) something we've agreed
to do as a team. I'm not sure I'd *want* to work on a software project where
code lands without review, but it's certainly possible to work that way. On the
other hand, if we've agreed to have a peer review process, then we need to
stick to that. We can't start waving through changes when we don't understand
them, or when only half the review comments have been addressed.

So, someone is going to have to review your code. Given that, it's important to
be mindful of the reviewer's time as well. As a team, there's no point an
author saving himself an hour if that means it's going to take a reviewer an
extra two hours to give an effective review.

And yes, I know we're busy. We're *always* busy though. If we make an exception
today, we end up making an exception every day.

The second answer to the "we don't have time for this" argument is that making
code easier to review actually leads to better code before we even get to the
review. I've lost count of the number of times I've tried to restructure a
changeset for review, and in the process, discovered a bug, or thought of a
cleaner way of making the changes. The process of revisiting my changes, and
having to justify them to myself, frequently makes me realise that I've messed
up somehow.

## Summary

Effective code review is important, but unless we as authors think about how to
make code easy to review, effective code review becomes almost impossible. It
can feel like a waste of time to rearrange our changes to make them easier to
review, but I believe that doing so is a critical part of writing good software.
