Title: Conventional Commits, considered harmful
Date: 2023-09-12 21:00
Summary: Why I'm not a fan of conventional commits.
Status: draft

Every so often, I get involved with a project that has decided to use
[conventional commits](https://www.conventionalcommits.org), and, invariably, I
wind up hating it.

## Background

The [website](https://www.conventionalcommits.org) explains the concept better
than I can, but the principle behind conventional commits is that you follow a
particular structure in your commit messages so that automated tooling can
interpret them. In particular, the summary line of your commit message should
include the *type* of commit (typically `feat` for new feature, `fix` for
bugfixes, or `chore` for... everything else), and, often, a *scope* describing
which part of the codebase is changing.

Here are a few examples from the
[lerna](https://github.com/lerna/lerna) git repository:

    :::text
    * f2f742b 2023-09-13 22:20:33 +0400 chore(misc): publish 7.3.0
    * c5079af 2023-09-13 20:17:24 +0200 chore(diff): enable strict type checking for diff command (#3838)
    * 3f01626 2023-09-11 12:44:36 -0600 chore: exclude package node_modules from git (#3830)
    * 196803d 2023-09-11 12:40:58 -0600 chore(version): add e2e test for --run-scripts-on-lockfile-update (#3831)
    * d477529 2023-09-11 12:40:12 -0600 fix(core): skip unnecessary cycles when running tasks (#3834)
    * 4940f2d 2023-09-11 19:50:32 +0200 fix(version): Fix crash when using `gitSignTag` with `independent` versioning mode (#3832)
    * 4843c3c 2023-09-06 16:22:52 -0500 feat(version): option to not ignore scripts on lock update (#3823)

With the exception of the `fix` and `feat` types, the Conventional Commits spec
leaves the choice of types and scopes up to individual projects, though `chore`
seems to be almost universally used to mean "things the end-user won't see"
(including refactoring and build process work).

This style of commit message appears to have been popularised by the
[Angular](https://github.com/angular/angular) project, who started using it
sometime in 2011 — though I'm sure they weren't the first people to have the
idea of embedding metadata in commit comments.

## `chore` is a problematic term

The thing that really grinds my gears about this whole process, on a daily
basis, is, in many ways, ridiculous. Here's how it goes. I'll be going through
my notifications on Github, and I'll see a pull request for a project I
maintain. Hurrah! We like contributions. But the summary of the PR is something
along the lines of:

    chore: clean up the FooFrobnicator

... and it seems like the contributor is *complaining* about having to make
this change! "I'm sorry, who forced you to start cleaning up my `FooFrobnicator`?"

Now, this is clearly a me problem. I should just get the hell over
it. It's just a label, right? Except... I think there's an important point
here. I don't know who came up with the idea of using `chore` to mean "everything
that's not a feature or a bugfix" (interestingly, it *wasn't* Angular, and the
Conventional Commits spec mentions `chore` only in a couple of examples), but I
think it was a really poor choice.

The [Cambridge
Dictionary](https://dictionary.cambridge.org/dictionary/english/chore)
describes a chore as "a job or piece of work that is *often boring or
unpleasant* but needs to be done regularly" (my emphasis).

So we're sending out the message to all our peers — including the next
generation of software engineers — that anything that isn't actively fixing a
bug or delivering a shiny new feature is *boring or unpleasant*.

I think this is deeply troubling messaging. Taking the time to clean up or
document code is not only absolutely critical, it is rewarding in its own
right, and something to be proud of. It can be hard to find time to do such
work in the face of pressing deadlines; we certainly don't need to find
ourselves another reason to skip it. So let's not give it a label that says to
ourselves and the rest of the world "this was a pain in the ass and you should
all be grateful to me for doing it".

## It's a terrible way to write changelogs

It's possible to use conventional commits without the use of the offensive
`chore`, but there are plenty of other reasons doing so is a bad
idea. Principal among them is: *I just don't see the point*. Or rather, the
reason that is normally top of the list (including on the [conventional
commits website](https://www.conventionalcommits.org/en/v1.0.0/#why-use-conventional-commits))
is just a *terrible idea*.

That reason: "Automatically generating CHANGELOGs".

"Now hold on Rich, changelogs are a [chore](#chore-is-a-problematic-term) to
maintain. We've got all the information we need in the commit messages. Why
wouldn't we automate them?"

Well yes, but also no. The fundamental problem is that commit messages and
changelogs are meant for completely different audiences. Commit messages are
meant to tell other *developers* (including your future self) which parts of
the code changed and how. They should talk in terms of classes and
modules. (You'll be unsurprised to learn I have Opinions on good commit
messages. But that's a post for another day.) Changelogs, on the other hand,
are meant for *users* of your application/library/product/service. Your users
are interested in bugfixes and new features. They don't know or want to know
which particular module had a bug, and they aren't interested in the series of
10 commits that were involved in landing the new feature.

In short, if you try and combine changelogs and commit messages into the same
thing — if you try to serve both your audiences with the same text — you'll end
up doing a bad job of both.


* wastes space (cf 50 char limit). Angular frequently violates this
* harder to read
* reverts are hard
