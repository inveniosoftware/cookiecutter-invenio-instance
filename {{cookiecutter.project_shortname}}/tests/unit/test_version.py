{% include 'misc/header.py' %}
"""Simple test of version import."""

from __future__ import absolute_import, print_function


def test_version():
    """Test version import."""
    from {{cookiecutter.package_name}} import __version__
    assert __version__
