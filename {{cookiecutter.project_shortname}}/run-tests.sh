#!/usr/bin/env bash
{% include 'misc/header.py' %}
# Ignoring false positive 36759 (reporting invenio-admin v1.0.1). This can be
# removed when https://github.com/pyupio/safety-db/pull/2274 is merged and
# released.
pipenv check --ignore 36759 && \
pipenv run pydocstyle {{ cookiecutter.package_name }} tests docs && \
pipenv run isort -rc -c -df && \
pipenv run check-manifest --ignore ".travis-*,docs/_build*" && \
pipenv run sphinx-build -qnNW docs docs/_build/html && \
pipenv run test
