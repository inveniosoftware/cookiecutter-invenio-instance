#!/usr/bin/env bash
{% include 'misc/header.py' %}
# Ignoring flask-admin XSS vulnerability 36437, remove when
# https://github.com/flask-admin/flask-admin/pull/1699 is merged an released.
pipenv check --ignore 36437 && \
pipenv run pydocstyle {{ cookiecutter.package_name }} tests docs && \
pipenv run isort -rc -c -df && \
pipenv run check-manifest --ignore ".travis-*,docs/_build*" && \
pipenv run sphinx-build -qnNW docs docs/_build/html && \
pipenv run test
