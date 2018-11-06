{% include 'misc/header.py' %}
"""{{ cookiecutter.description }}"""

import os

from setuptools import find_packages, setup

readme = open('README.rst').read()

INVENIO_VERSION = "3.1.0.dev20181106"

packages = find_packages()


# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('{{ cookiecutter.package_name }}', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='{{ cookiecutter.project_shortname }}',
    version=version,
    description=__doc__,
    long_description=readme,
    keywords='{{ cookiecutter.project_shortname }} Invenio',
    license='MIT',
    author='{{ cookiecutter.author_name }}',
    author_email='{{ cookiecutter.author_email }}',
    url='https://github.com/{{ cookiecutter.github_repo }}',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.project_shortname }} = invenio_app.cli:cli',
        ],
        'invenio_base.apps': [
            'flask_debugtoolbar = flask_debugtoolbar:DebugToolbarExtension',
        ],
        'invenio_base.blueprints': [
            '{{ cookiecutter.package_name }} = {{ cookiecutter.package_name }}.views:blueprint',
        ],
        'invenio_config.module': [
            '{{ cookiecutter.package_name }} = {{ cookiecutter.package_name }}.config',
        ],
        'invenio_i18n.translations': [
            'messages = {{ cookiecutter.package_name }}',
        ]
    },
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 3 - Alpha',
    ],
)
