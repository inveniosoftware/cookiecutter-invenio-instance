#!/usr/bin/env bash
invenio db destroy --yes-i-know
invenio db init create
invenio index queue init
invenio index init
