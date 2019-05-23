{% include 'misc/header.py' %}
"""Permissions for {{ cookiecutter.project_name }}."""


def files_permission_factory(obj, action=None):
    """Permissions factory for buckets."""
    class Permission():
        def can(*args):
            return True

    return Permission()
