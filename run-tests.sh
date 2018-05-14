#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

# quit on errors:
set -o errexit

# quit on unbound symbols:
set -o nounset

WORKDIR=$(mktemp -d)

function finish {
    echo "Cleaning up."
    pip uninstall -y generated_fun
    rm -rf "${WORKDIR}"
}

trap finish EXIT

sphinx-build -qnN docs docs/_build/html
cookiecutter --no-input -o "$WORKDIR" . \
    project_name=Generated-Fun \
    database=postgresql \
    elasticsearch=elasticsearch6

cd "${WORKDIR}/generated-fun"

git init
git add -A

pip install -e .\[all\] --quiet

check-manifest -u || true

./run-tests.sh
