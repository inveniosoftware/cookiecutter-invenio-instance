{% include 'misc/header.py' %}
"""Flask extension for {{ cookiecutter.project_name }}."""

from __future__ import absolute_import, print_function

from . import config


class {{ cookiecutter.datamodel_extension_class }}(object):
    """{{ cookiecutter.project_name}} extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        self.init_config(app)
        app.extensions['{{ cookiecutter.project_shortname}}'] = self

    def init_config(self, app):
        """Initialize configuration.

        Override configuration variables with the values in this package.
        """
        with_endpoints = app.config.get(
            '{{ cookiecutter.package_name | upper }}_ENDPOINTS_ENABLED', True)
        for k in dir(config):
            if k.startswith('{{ cookiecutter.package_name | upper }}_'):
                app.config.setdefault(k, getattr(config, k))
            elif k == 'SEARCH_UI_JSTEMPLATE_RESULTS':
                app.config['SEARCH_UI_JSTEMPLATE_RESULTS'] = getattr(
                    config, k)
            elif k == 'PIDSTORE_RECID_FIELD':
                app.config['PIDSTORE_RECID_FIELD'] = getattr(config, k)
            elif k == 'FILES_REST_PERMISSION_FACTORY':
                app.config['FILES_REST_PERMISSION_FACTORY'] = getattr(config, k)
            else:
                for n in ['RECORDS_REST_ENDPOINTS', 'RECORDS_UI_ENDPOINTS',
                          'RECORDS_REST_FACETS', 'RECORDS_REST_SORT_OPTIONS',
                          'RECORDS_REST_DEFAULT_SORT',
                          'RECORDS_FILES_REST_ENDPOINTS']:
                    if k == n and with_endpoints:
                        app.config.setdefault(n, {})
                        app.config[n].update(getattr(config, k))
