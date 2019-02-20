# This is the Dockerfile that builds a fully functional image of your app
{% include 'misc/header.py' %}
ARG DEPENDENCIES_VERSION=latest
# Get the previously built image(Docker.base) with pip dependencies and extend it
FROM {{cookiecutter.project_shortname}}-base:${DEPENDENCIES_VERSION}

COPY ./ .
COPY ./docker/uwsgi/ ${INVENIO_INSTANCE_PATH}
# install the app
RUN pipenv run pip install .
# build your app's assets
RUN pipenv run invenio collect -v
RUN pipenv run invenio webpack create
RUN pipenv run invenio webpack install --unsafe
RUN pipenv run invenio webpack build

ENTRYPOINT [ "bash", "-c"]
