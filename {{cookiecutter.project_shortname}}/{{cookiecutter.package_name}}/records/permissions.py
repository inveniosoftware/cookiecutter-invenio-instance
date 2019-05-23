{% include 'misc/header.py' %}
"""Permissions for {{ cookiecutter.project_name }}."""

from invenio_access import Permission, any_user


def files_permission_factory(obj, action=None):
    """Permissions factory for buckets."""
    return Permission(any_user)
