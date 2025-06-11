Title: Managing release branches
Date: 2025-06-11 12:00
Summary: The one true way to do hotfix releases.

<!--
Clean up SVG from mermaidchart to edit in inkscape:
xmllint --format img2.svg | perl -pe 's/#export-svg :root{--mermaid.*?}//' > img2.0.svg

(ultimately we could move the styling to a separate file, but we need it there
to edit in inkscape for now.)
-->


One of the projects I'm involved with at work recently had cause to put out a
hotfix release, and I assumed that everyone agreed that it was obvious how we
should handle the git branches. Turns out, everyone *did* think it was obvious,
but the obvious solution was different for different people.

Let's suppose that we've got a relatively new project, but one in which we've
already cut the first release, and then carried on work:

<!--
https://www.mermaidchart.com/play#pako:eNp9jUsOgkAMhq9Sm0xmBcHtXMC4MPEA3TRQoWEYyFB1Qbi7YNxpXH7_c8F6bAQDFkVBydSiBEpvcG7RpBZgAW-dDOID-CR3yxw9rLA6R6lVO2WeOkoAUI_DoAbaBCA8b13l-BEJvxMX7gU2eo65_-Vfs0ycBR7HsoIsUXiWAyEYt7u9y2X1b_jG83aM6ws94Ukx
-->
<img alt="We have tagged 'v1.0.0' on 'main', then made another commit." src="{attach}release-branches/img1.svg" style="max-width: 600px;" >

Unfortunately, it turns out that our v1.0.0 has a critical bug, and we're going
to have to cut another release quickly. At times like this, we don't want to
risk making the situation worse by releasing new, relatively untested changes:
we just want to get the bugfix out there as soon as possible: we need a patch
release.

Git offers us two basic ways to approach this. I'll describe both, then explain
which I prefer and why.

## Fix on `main`, then backport

Option one is the "backport" strategy. We commit our fix to the mainline, then
we create a "release" branch, and cherry-pick the fix onto it, and finally cut
the release. It looks like this:

<!--
https://www.mermaidchart.com/play#pako:eNp9TjsOgkAQvcq4CaHCgOVewFiYeIBtRhjZCbCQZdCCcHdBwULE8v1fr9I6I6VVFEXGCUtJ2rgXCIKeHYuGHkKxVFGoIXTUiccyhAGGIDAuZzl6bKxxAJDWVcUCnGkw6jRmGcuZNGrtOGNBMKJH7Ytf-sVTg57gnuxj8FQStrQzCgTzSZ7ofTwHrx5dahdXNGnvQktpUXcCFbLbvnDD9u9Fz7n9GJbK9dhm9PB1O5m61PAEMOl6ZA
-->
<img alt="We have added a fix commit to 'main', then cherry-picked it to a release branch based on 'v1.0.0'." src="{attach}release-branches/cherry-pick.svg" style="max-width: 926px;" >


## Fix on release branch, then merge

The second approach goes the other way around: we first commit our fix to a
release branch, and then we *merge* it onto main:

<!--
https://www.mermaidchart.com/play#pako:eNp1js0OgkAMhF-lbkI4QeS6L2A8mPgAe6lY2QZ2IbXqgfDugoKJf8fOzDed3pTtkYw1WZa5qKwNWRcfR5L0HFkt9JCqp0CphTTSRQWbFAYYksTFinUj2HkXAaBsQ2AFPlpwZjuyjM0sOvOd2GFNMF63Vupf_l6oQyG4FvkahBrCM62cAcVqsic5X8_gQTCWfkllk_cs9FTW7UUhIMf_E054fk1ciO-uX6Rw5fVjVPFZ9XoeSCp6azbDHZASfGs
-->
<img alt="We have created a release branch based on 'v1.0.0' where we have committed a fix. We have then merged the release branch into 'main'." src="{attach}release-branches/merge.svg" style="max-width: 926px;" >

## What's to choose

The good thing about the "backport" approach is that it mirrors your normal way
of working: developers take the latest `main` and make their changes there. You
may have CI which only runs against `main`. By developing against `main`, the
logic goes, you have the best chance of picking up problems in your fix.

On the other hand, what happens if there are significant differences between
`v1.0.0` and `main`, such that a fix on one branch won't apply cleanly to the
other? In that case, we're going to have to do extra work — in the worst case,
we might end up writing two completely separate fixes for the two branches — in
which case, we don't really get that "normal way of working" benefit. Instead,
we have delayed our patch release by spending all that time developing a fix
for `main`.

With the "merge" approach, we write the fix for the release branch, then cut
the release, and only *then* do we worry about how to apply the fix to
`main`. Ultimately, our urgent fix lands in users' hands more quickly.

There's a second advantage to the "merge" approach, and it ties into git branch
management in general[ref]A topic on which I, as ever, have Opinions, but I will sharte them another day[/ref] have plenty . In short, I prefer to merge release branches into `main`
after the release is complete, for regular releases as well as hotfixes.

<!--
https://www.mermaidchart.com/play#pako:eNp9jksOgkAMhq9SJyGsMOByLmBcmHiA2VSsTAMzmFp1Qbi7ouACH8v-j69_Z8r2QMaaLMtcVNaGrIvPI0k6jqwWOkjVU6DUQhrpooJNCj30SeJixboWPHkXAaBsQ2AFPlhwZvPoMjaj6MxnYos1weO6tVJ_83dCJxSCa7HMQaghPNPCGVCsBnuQl_lY3AvG0k-pbPBeQE9l3V4UAnL8PeGI578ThSv_DkzIz2c_q6vZ7GLOes8LJBXN0Ka_A-pfiBY
-->

This helps to ensure that any last-minute changes on the release branch
(version bumps, changelog updates, etc) make it back into `main` and hence into
future releases. More to the point, I can look at a git revision tree[ref]`git
log --graph` for the win[/ref] and instantly see that everything in the release
made it back to `main`.

So how does this relate to hotfix releases? Two ways. First, I end up with a
cleaner git history by committing the fix to the release branch first and then
merging: specifically, the fix only appears once in the git revision
tree. Second, in the case where there are conflicts between the fix and `main`,
if I commit the fix to main first, then I'm going to end up handling those
conflicts twice: once when I cherry-pick the fix to the release branch, and
*again* when I merge the release branch to `main`.

## Conclusion

To wrap up, then: if I need to develop a hotfix, I much prefer to develop it
against the stable release in the first instance, rather than backporting from
`main`. Doing so lets me get the fix into the hands of users quicker, and
leaves me with a cleaner git history.

There might be times where that's not possible (in particular: the fix has
already happened and only later do we realise it needs backporting). That's
fine: I'm just talking about a preference, not an eleventh commandment.

Of course, developing against a release branch might necessitate fixing your CI
so that runs against release branches as well as `main`, but I think that's a
good thing to do anyway.

## Finally

While I was writing this, my colleague [@poljar](https://github.com/poljar)
pointed out that the Linux Kernel does the opposite of what I suggest. He's
right, of course, but I'm prepared to give them a pass. The kernel is an
unusual project in many ways, and what works for them won't necessarily work
well for Normal™ projects.

# Acknowledgements

The graphs on this page are rendered with
[Mermaid](https://mermaid.js.org/syntax/gitgraph.html) and then lightly edited
in [Inkscape](https://inkscape.org/).
