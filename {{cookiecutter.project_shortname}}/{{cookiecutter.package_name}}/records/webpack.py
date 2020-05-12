{% include 'misc/header.py' %}
"""JS/CSS Webpack bundle to override search results template."""

from invenio_assets.webpack import WebpackThemeBundle

search_app = WebpackThemeBundle(
    __name__,
    'assets',
    default='semantic-ui',
    themes={
        'semantic-ui': dict(
            entry={
                '{{ cookiecutter.project_shortname }}-search-app': './js/{{ cookiecutter.package_name }}/records/search_app_customizations.js',
            },
            dependencies={}
        )
    }
)
