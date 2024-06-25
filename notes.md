Ops
---
Build to `output`: `pelican`
Build with prod settings: `pelican -s publishconf.py`
Start local server: `pelican -lr`

Theming
-------

We're usung the
[pelican-bootstrap3](https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3)
pelican theme, itself with the `cerulean` bootstrap theme. There is also a bit of custom css.


TODO
----

* (done) Expand `about` page
* (done) Find a better theme
  - no categories
  - decluttered front page
* (done) write an article
* (done) Improve appearance
  - Serif font. And bigger.
  - De-uglify date thingio
* (done) write an article

* can we avoid git-cloning the plugins repo?
  https://github.com/pelican-plugins/simple-footnotes suggests we can just pip install
* consider making `label-default` `visibility: none`
* (done) link from richvdh.org
* Write a readme

Ideas
-----
 * the importance of comments.
   * Don't make me reverse-engineer stuff.
   * helps write better code
 * the importance of small PRs
   * make it easy on the reviewer
   * helps write better code
