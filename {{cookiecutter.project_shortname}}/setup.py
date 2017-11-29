{% include 'misc/header.py' %}
"""{{ cookiecutter.description }}"""

import os

from setuptools import find_packages, setup

readme = open('README.rst').read()
history = open('CHANGES.rst').read()

tests_require = [
    'check-manifest>=0.35',
    'coverage>=4.4.1',
    'isort>=4.2.15',
    'mock>=2.0.0',
    'pydocstyle>=2.0.0',
    'pytest-cache>=1.0',
    'pytest-cov>=2.5.1',
    'pytest-flask>=0.10.0',
    'pytest-mock>=1.6.0',
    'pytest-pep8>=1.0.6',
    'pytest-random-order>=0.5.4',
    'pytest>=3.1.3',
    'selenium>=3.5.0,<3.6.0',
    'six>=1.10.0',
]

db_version = '~1.0.0'
search_version = '~1.0.0'

extras_require = {
    'docs': [
        'Sphinx>=1.5.1',
    ],
    'tests': tests_require,
    # Database version
    'postgresql': [
        'invenio-db[postgresql,versioning]{}'.format(db_version),
    ],
    'mysql': [
        'invenio-db[mysql,versioning]{}'.format(db_version),
    ],
    'sqlite': [
        'invenio-db[versioning]{}'.format(db_version),
    ],
    # Elasticsearch version
    'elasticsearch2': [
        # 'invenio-search[elasticsearch2]{}'.format(search_version),
        'elasticsearch~=2.0',
        'elasticsearch-dsl~2.0',
    ],
    'elasticsearch5': [
        # 'invenio-search[elasticsearch5]{}'.format(search_version),
        'elasticsearch~=5.0',
        'elasticsearch-dsl~=5.0',
    ],
}

extras_require['all'] = []
for name, requirements in extras_require.items():
    if name in ('sqlite', 'mysql', 'postgresql') \
            or name.startswith('elasticsearch'):
        continue
    extras_require['all'].extend(requirements)

setup_requires = [
    'Babel>=2.4.0',
    'pytest-runner>=2.7.0',
]

install_requires = [
    'Flask-BabelEx>=0.9.2',
    'Flask-Debugtoolbar>=0.10.1',
    'invenio[base,auth,metadata]~=3.0.0',
]

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
    long_description=readme + '\n\n' + history,
    keywords='{{ cookiecutter.project_shortname }} invenio TODO',
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
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Development Status :: 3 - Alpha',
    ],
)
