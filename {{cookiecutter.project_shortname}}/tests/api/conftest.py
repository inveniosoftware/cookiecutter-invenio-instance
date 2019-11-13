{% include 'misc/header.py' %}
"""Pytest fixtures and plugins for the API application."""

from __future__ import absolute_import, print_function

import tempfile

import pytest
from invenio_app.factory import create_api
from invenio_files_rest.models import Location


@pytest.fixture(scope='module')
def create_app():
    """Create test app."""
    return create_api


@pytest.fixture()
def location(app, db):
    """Create default location."""
    tmppath = tempfile.mkdtemp()
    with db.session.begin_nested():
        Location.query.delete()
        loc = Location(name="local", uri=tmppath, default=True)
        db.session.add(loc)
    db.session.commit()
    return loc
