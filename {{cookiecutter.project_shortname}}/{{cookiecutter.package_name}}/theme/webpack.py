{% include 'misc/header.py' %}
"""JS/CSS Webpack bundles for theme."""

from invenio_assets.webpack import WebpackThemeBundle

theme = WebpackThemeBundle(
    __name__,
    'assets',
    default='semantic-ui',
    themes={
        'bootstrap3': dict(
            entry={
                '{{ cookiecutter.project_shortname }}-theme': './scss/{{ cookiecutter.package_name }}/theme.scss',
                '{{ cookiecutter.project_shortname }}-preview': './js/{{ cookiecutter.package_name }}/previewer.js',
            },
            dependencies={},
            aliases={},
        ),
        'semantic-ui': dict(
            entry={
                '{{ cookiecutter.project_shortname }}-preview': './js/{{ cookiecutter.package_name }}/previewer.js',
            },
            dependencies={
                # add any additional npm dependencies here...
            },
            aliases={
                '../../theme.config$': 'less/{{ cookiecutter.package_name }}/theme.config',
            },
        ),
    }
)
