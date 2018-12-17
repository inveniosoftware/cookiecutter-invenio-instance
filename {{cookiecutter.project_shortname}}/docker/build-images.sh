#!/usr/bin/env bash
{% include 'misc/header.py' %}

script_path=$(dirname "$0")

pipfile_lock_path="$script_path/../Pipfile.lock"

if [ ! -f $pipfile_lock_path ]; then
    echo "'Pipfile.lock' not found. Generate it by running 'pipenv lock'."
    exit 1
fi

# Extract Pipfile.lock hash to use as the docker image tag
deps_ver=$(cat $pipfile_lock_path | python -c "import json,sys;print(json.load(sys.stdin)['_meta']['hash']['sha256'])")

# Build dependencies image
docker build -f Dockerfile.base -t {{cookiecutter.project_shortname}}-base:$deps_ver .

# Build application image
docker build --build-arg DEPENDENCIES_VERSION=$deps_ver . -t {{cookiecutter.project_shortname}}
