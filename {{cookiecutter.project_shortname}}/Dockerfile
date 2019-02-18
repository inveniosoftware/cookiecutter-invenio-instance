{% include 'misc/header.py' %}
ARG DEPENDENCIES_VERSION=latest
FROM {{cookiecutter.project_shortname}}-base:${DEPENDENCIES_VERSION}

COPY ./ .
COPY ./docker/uwsgi/ ${INVENIO_INSTANCE_PATH}

RUN ./scripts/bootstrap --deploy

ENTRYPOINT ["bash", "-c"]
