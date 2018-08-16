{% include 'misc/header.py' %}
FROM {{cookiecutter.project_shortname}}-base:latest

COPY ./ .
COPY ./docker/uwsgi/ ${INVENIO_INSTANCE_PATH}

RUN ./scripts/bootstrap

USER ${INVENIO_USER_ID}
