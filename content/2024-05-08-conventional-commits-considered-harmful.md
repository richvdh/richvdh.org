Title: Conventional Commits, considered harmful
Date: 2023-09-12 21:00
Summary: Why I'm not a fan of conventional commits.

Every so often, I get involved with a project that has decided to use
[conventional commits](https://www.conventionalcommits.org), and, invariably, I
wind up hating it.

## Conventional whatnow?

In case you've managed to avoid this idea so far, let's start with a quick
explainer about what conventional commits actually involves.

The [website](https://www.conventionalcommits.org) explains the concept better
than I can, but the principle is that you follow a particular structure in your
commit messages. In particular, the summary line of your commit message should
include the *type* of commit (typically `feat` for new feature, `fix` for
bugfixes, or `chore` for... everything else), and, often, a *scope* describing
which part of the codebase is changing.

Here are a few examples from the
[lerna](https://github.com/lerna/lerna) Git repository:

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
idea of embedding metadata in commit comments. I'll call out Angular a few
times in this post by way of examples, but I don't mean to dunk on them
particularly — there are plenty of other projects which follow similar
patterns.

## `chore` is a problematic term

The thing that really grinds my gears about this whole process is, in some
ways, trivial. Here's how it goes. I'll be going through my notifications on
Github, and I'll see a pull request for a project I maintain. Hurrah! We like
contributions. But the summary of the PR is something along the lines of the following:

    chore: clean up the FooFrobnicator

The [Cambridge
Dictionary](https://dictionary.cambridge.org/dictionary/english/chore)
describes a chore as "a job or piece of work that is *often boring or
unpleasant* but needs to be done regularly" (my emphasis). So it seems like the
contributor is *complaining* about having to make this change! "I'm sorry, who
forced you to start cleaning up my `FooFrobnicator`?"

Now, this is clearly a me problem. I should just get the hell over it. It's
just a label, right? Except... I think there's an important point here. I don't
know who came up with the idea of using `chore` to mean "everything that's not
a feature or a bugfix" [ref]It *wasn't* Angular, and the Conventional Commits
spec mentions `chore` only in a couple of examples.[/ref], but I believe it was
a really poor choice. By using this term, we're sending out the message to all
our peers — including the next generation of software engineers — that anything
that isn't actively fixing a bug or delivering a shiny new feature is *boring
or unpleasant*.

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
is just a *terrible idea*. That reason: "Automatically generating CHANGELOGs".

"Now hold on Rich, changelogs are a *chore* to maintain. We've got all the
information we need in the commit messages. Why wouldn't we automate them?"

Well yes, but also no. The fundamental problem is that commit messages and
changelogs are meant for completely different audiences. Commit messages are
meant to tell other *developers* (including your future self) which parts of
the code changed and how. They should talk in terms of classes and
modules[ref]You'll be unsurprised to learn I have Opinions on good commit
messages. But that's a post for another day.[/ref]. They start with a *brief*
summary line "Fix accidental frobnication in `frobnicateDowhacky()`" and go on
to explain more detail about why and how the change happened.

Changelogs, on the other hand, are meant for *users* of your
application/library/product/service. Your users are interested in bugfixes and
new features. They don't know or want to know which particular module had a
bug, and they aren't interested in the series of 10 commits that were involved
in landing the new feature. Also, changelogs aren't subject to the same
formatting constraints as commit messages.

In short, if you try and combine changelogs and commit messages into the same
thing — if you try to serve both your audiences with the same text — you'll end
up doing a bad job of both. Normally it's the changelog that suffers most; it
just becomes list of low-level changes that are meaningless to users.

At the end of the day: if I just wanted a list of your commit messages, I'd run
`git log`. You've told yourself you're being a responsible maintainer by
maintaining a changelog, but that's not what you're doing. There's a lot more
to maintaining a good changelog than pasting your commit messages into a text
document[ref]I also have Opinions on good tooling for maintaining
changelogs. Also a post for another day.[/ref].

## It's a waste of space

Speaking of formatting commit messages, there are some conventions that Git
commit messages are meant to
follow. [This blog post](https://cbea.ms/git-commit/#seven-rules) is a great
explanation.

Anyway, there is a common guideline that the subject line of a commit message
should ideally be limited to about 50 characters, and that 72 characters should
be considered a pretty hard limit.

Now, if the first 30 characters of your commit message subject are
`chore(dowhacky-controller): `, that doesn't leave a whole lot of space for
describing what's actually changed. It's worth noting that Angular's commit
messages frequently violate the 72-character limit.

Of course, writing a useful summary of a change in 50 or even 72 characters can
be *hard*, and this is actually an area where a `scope: ` prefix can be quite
helpful. It's just that sometimes more flexibility can be useful, and the
"type" part of the conventional commit format wastes valuable space.

In short: I argue that *requiring* all commits to use a fixed format limits
contributors' ability to write effective, concise commit summaries.

## Reverts are hard

This is really a special-case of "it's a terrible way to write changelogs," but
it's so egregious I wanted to call it out separately.

Let's suppose you've added a new feature to your application, and proudly
landed it with a commit message `feat(ui): Add new DowhackyManager
interface`. But before you release it, you realise that it breaks some other
part of the system, and decide to revert it while you iron out the kinks.

The question is: what should you write in the commit message for the revert?
Conventional commits doesn't really offer much advice here. Maybe you could go
with Git's default (`revert "feat(ui): ..."`), but it doesn't really matter.

The problem comes when you come to turn this into a changelog. Unless your
commit-to-changelog tooling is really clever[ref]`git-cliff`, for instance,
[doesn't yet support it](https://github.com/orhun/git-cliff/issues/382)[/ref],
what the readers of your changelog are going to see is that your new release
contains your shiny new feature. Which is just wrong.

We might be able to add enough magic to the tooling to fix this problem, but
wouldn't it be better if we could just revert the changelog update alongside
the code change?

## It's frequently impractical

Conventional commits encourages you to define a "scope" for each commit. The
problem is that, in practice, commits frequently end up spanning multiple
scopes. So if you're using those scopes to produce changelogs for the different
parts of your system, you're in a bit of an awkward spt.

"That just means your change needed breaking down into smaller commits." Well,
maybe. I am a big fan of small, atomic commits[ref]Yet another post for
another day[/ref]. But if I have to choose
between one commit that touches one line in each of two files, and a series of
commits that introduces a compatibility shim, uses it in various places, then
eventually removes the shim again... well, that's not much of a choice.
**And that decision shouldn't be driven by some wrong-headed desire to
generate changelogs from commit messages.**

## TL;DR

The conventional commits style can be a good way to write a succinct commit
subject line. That's cool, and I absolutely encourage its use where it
helps. (Please don't label everything as a chore, though.) But I don't think
mandating it serves anyone well; and I *really* disagree with using commit
message to generate a changelog.
