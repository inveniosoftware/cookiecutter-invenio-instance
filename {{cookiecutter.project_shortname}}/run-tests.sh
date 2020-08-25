#!/usr/bin/env bash
{% include 'misc/header.py' %}

pipenv check && \
pipenv run pydocstyle {{ cookiecutter.package_name }} tests docs && \
pipenv run isort . --check-only --diff && \
pipenv run check-manifest --ignore ".travis-*,docs/_build*" && \
pipenv run sphinx-build -qnNW docs docs/_build/html && \
pipenv run test
