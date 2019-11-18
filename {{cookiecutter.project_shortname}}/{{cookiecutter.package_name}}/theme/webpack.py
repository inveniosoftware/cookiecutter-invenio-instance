{% include 'misc/header.py' %}
"""JS/CSS Webpack bundles for theme."""

from __future__ import absolute_import, print_function

from flask_webpackext import WebpackBundle

theme = WebpackBundle(
    __name__,
    'assets',
    entry={
        '{{ cookiecutter.project_shortname }}-theme': './scss/{{ cookiecutter.package_name }}/theme.scss',
        '{{ cookiecutter.project_shortname }}-preview': './js/{{ cookiecutter.package_name }}/previewer.js',
    },
    dependencies={
        # add any additional npm dependencies here...
    }
)
