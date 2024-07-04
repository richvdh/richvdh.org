This is the source for my personal blog, [richvdh.org](https://richvdh.org).

Operational notes
-----------------

The site is built with [Pelican](http://docs.getpelican.com/).

To build it, first install the dependencies:

```sh
git submodule update --init
python -m venv env
./env/bin/pip install -r requirements.txt
```

Then:

* `./env/bin/pelican` will build a static copy of the site in the `output`
  directory.
* `./env/bin/pelican -lr` will start a development server, exposing the
  generated site at `http://localhost:8000`.

Theming
-------

The site is themed with the
[pelican-bootstrap3](https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3)
pelican theme, itself with the `cerulean` bootstrap theme. There is also a bit
of [custom css](content/extra/custom.css).
