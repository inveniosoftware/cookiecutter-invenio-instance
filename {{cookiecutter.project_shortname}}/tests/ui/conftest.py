{% include 'misc/header.py' %}
"""Pytest fixtures and plugins for the UI application."""

import pytest
from invenio_app.factory import create_ui


@pytest.fixture(scope='module')
def create_app():
    """Create test app."""
    return create_ui
