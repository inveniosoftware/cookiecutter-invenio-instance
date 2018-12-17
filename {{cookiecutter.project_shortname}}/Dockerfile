{% include 'misc/header.py' %}
ARG DEPENDENCIES_VERSION=latest
FROM {{cookiecutter.project_shortname}}-base:${DEPENDENCIES_VERSION}

COPY ./ .
COPY ./docker/uwsgi/ ${INVENIO_INSTANCE_PATH}

RUN pipenv run pip install .

RUN pipenv run invenio collect -v
RUN pipenv run invenio webpack create
RUN pipenv run invenio webpack install --unsafe
RUN pipenv run invenio webpack build
