#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE USER zenodo WITH CREATEDB PASSWORD '{{cookiecutter.package_name}}';
    CREATE DATABASE {{cookiecutter.package_name}} OWNER {{cookiecutter.package_name}};
    GRANT ALL PRIVILEGES ON DATABASE {{cookiecutter.package_name}} TO {{cookiecutter.package_name}};
EOSQL
