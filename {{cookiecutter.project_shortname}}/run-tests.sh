#!/usr/bin/env bash
{% include 'misc/header.py' %}

# Usage:
#   env DB=postgresql ./run-tests.sh

# Quit on errors
set -o errexit

# Quit on unbound symbols
set -o nounset

python -m check_manifest --ignore ".*-requirements.txt"
python -m sphinx.cmd.build -qnNW docs docs/_build/html
# TODO: Pass the services required by your module to the
# docker-services-cli e.g. `docker-services-cli up es postgresql redis`
# remove docker-services-cli if you don't need any of the services.
docker-services-cli up
python -m pytest
python -m sphinx.cmd.build -qnNW -b doctest docs docs/_build/doctest
tests_exit_code=$?
