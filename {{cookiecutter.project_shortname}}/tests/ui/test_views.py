{% include 'misc/header.py' %}
"""Views tests."""

from __future__ import absolute_import, print_function

from flask import url_for


def test_ping(client):
    """Test the ping view."""
    resp = client.get(url_for('{{cookiecutter.package_name}}.ping'))
    assert resp.status_code == 200
    assert resp.get_data(as_text=True) == 'OK'
