{% include 'misc/header.py' %}
"""JS/CSS Webpack bundle to override search results template."""

from invenio_assets.webpack import WebpackThemeBundle

search_app = WebpackThemeBundle(
    __name__,
    'assets',
    default='semantic-ui',
    themes={
        'bootstrap3': dict(entry={}, dependencies={}, aliases={}),
        'semantic-ui': dict(
            entry={
                '{{ cookiecutter.project_shortname }}-search-app':
                './js/{{ cookiecutter.package_name }}_records/index.js',
            },
            dependencies={
                "react": "^16.9.0",
                "react-dom": "^16.9.0",
                "react-overridable": "^0.0.2",
                "semantic-ui-react": "^0.88.0"
            }
        )
    }
)
