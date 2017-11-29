#!/usr/bin/env bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE ROLE {{cookiecutter.project_shortname}} WITH LOGIN PASSWORD '{{cookiecutter.project_shortname}}';
    ALTER ROLE {{cookiecutter.project_shortname}} CREATEDB;
    \du;
EOSQL
