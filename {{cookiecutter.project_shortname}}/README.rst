{% include 'misc/header.rst' %}
{{ '=' * (cookiecutter.project_name|length + 2) }}
 {{ cookiecutter.project_name }}
{{ '=' * (cookiecutter.project_name|length + 2) }}

.. image:: https://github.com/{{ cookiecutter.github_repo }}/workflows/CI/badge.svg
        :target: https://github.com/{{ cookiecutter.github_repo }}/actions?query=workflow%3ACI

.. image:: https://img.shields.io/github/license/{{ cookiecutter.github_repo }}.svg
        :target: https://github.com/{{ cookiecutter.github_repo }}/blob/master/LICENSE

{{ cookiecutter.description }}

Further documentation is available on
https://{{ cookiecutter.project_shortname }}.readthedocs.io/

