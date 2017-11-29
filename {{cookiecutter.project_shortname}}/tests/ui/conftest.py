{% include 'misc/header.py' %}
"""Pytest fixtures and plugins for the UI application."""

from __future__ import absolute_import, print_function

from invenio_app.factory import create_ui


@pytest.fixture(scope='module')
def create_app():
    return create_ui
