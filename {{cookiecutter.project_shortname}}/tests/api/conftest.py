{% include 'misc/header.py' %}
"""Pytest fixtures and plugins for the API application."""

from __future__ import absolute_import, print_function

from invenio_app.factory import create_api


@pytest.fixture(scope='module')
def create_app():
    return create_api
