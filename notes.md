Ops
---
Build: `pelican`
Build with prod settings: `pelican -s publishconf.py`
Start local server: `pelican -lr`

TODO
----

* (done) Expand `about` page
* (done) Find a better theme
  - no categories
  - decluttered front page

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
