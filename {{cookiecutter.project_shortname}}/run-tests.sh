#!/usr/bin/env bash
{% include 'misc/header.py' %}
pydocstyle {{ cookiecutter.package_name }} tests docs && \
isort -rc -c -df && \
check-manifest --ignore ".travis-*,docs/_build*" && \
sphinx-build -qnNW docs docs/_build/html && \
python setup.py test
