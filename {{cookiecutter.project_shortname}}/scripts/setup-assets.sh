#!/usr/bin/env bash
CWD=`pwd`
invenio npm
cd ${VIRTUAL_ENV}/var/instance/static
npm install
cd ${CWD}
invenio collect -v
invenio assets build
