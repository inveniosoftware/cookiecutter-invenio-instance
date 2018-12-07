{% include 'misc/header.py' %}
FROM {{cookiecutter.project_shortname}}-base:latest

COPY ./ .

RUN pipenv run pip install .

RUN pipenv run invenio collect -v
RUN pipenv run invenio webpack create
RUN pipenv run invenio webpack install --unsafe
RUN pipenv run invenio webpack build
