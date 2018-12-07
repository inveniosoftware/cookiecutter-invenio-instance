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

finish (){
    echo "Cleaning up."
    docker-compose down --volumes --remove-orphans &
    pipenv --rm || true
    rm -rf "${WORKDIR}"
}

deploy_cluster() {
    docker build -f Dockerfile.dev.base -t my-site-base .
    docker build . -t my-site -t my-site-web-api -t my-site-web-ui -t my-site-worker
    docker-compose -f docker-compose.full.yml up -d
    ./docker/wait-for-services.sh
}

trap finish EXIT

PROJECT_NAME="my-site"

cookiecutter --no-input -o "$WORKDIR" . \
    project_name=${PROJECT_NAME} \
    database=${COOKIECUTTER_DATABASE:-postgresql} \
    elasticsearch=${COOKIECUTTER_ELASTICSEARCH:-elasticsearch6}

cd "${WORKDIR}/${PROJECT_NAME}"
pipenv lock --pre

deploy_cluster
./docker/wait-for-services.sh
echo "All services are up."
git init
git add -A
# check that instance can be started locally as well
./scripts/bootstrap

pipenv run check-manifest -u || true
