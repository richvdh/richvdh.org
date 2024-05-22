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
