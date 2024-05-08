Ops
---
Build to `output`: `pelican`
Build with prod settings: `pelican -s publishconf.py`
Start local server: `pelican -lr`

Theming
-------

We're usung [pelican-bootstrap3](https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3).

Some themes are available from https://bootswatch.com/ (todo: try a few more?),
but none of them seem to use a serif font. Probably we need a custom CSS file?
Or to fork a theme?




TODO
----

* (done) Expand `about` page
* (done) Find a better theme
  - no categories
  - decluttered front page
* (done)_write an article
* Improve appearance
  - Serif font. And bigger.
  - De-uglify date thingio

* write an article

* can we avoid git-cloning the plugins repo?
  https://github.com/pelican-plugins/simple-footnotes suggests we can just pip install

* consider making `label-default` `visibility: none`

* Figure out how to publish to Gitlab pages
  (https://about.gitlab.com/blog/2016/04/07/gitlab-pages-setup/)

  * we should use gitlab, because supporting the little guy is nice
  * `make gitlab` uses `ghp-import`. But gitlab pages uses a different
    mechanism?

* link from richvdh.org
* Write a readme
