#
# {{ cookiecutter.project_name }} docker build
#
FROM python:3.5
MAINTAINER {{ cookiecutter.author_name }} <{{ cookiecutter.author_email }}>

ARG TERM=linux
ARG DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update \
    && apt-get -qy upgrade --fix-missing --no-install-recommends \
    && apt-get -qy install --fix-missing --no-install-recommends \
        apt-utils curl libcairo2-dev fonts-dejavu libfreetype6-dev \
    # Node.js
    && curl -sL https://deb.nodesource.com/setup_6.x | bash - \
    && apt-get -qy install --fix-missing --no-install-recommends \
        nodejs \
    # Slim down image
    && apt-get clean autoclean \
    && apt-get autoremove -y \
    && rm -rf /var/lib/{apt,dpkg}/ \
    && rm -rf /usr/share/man/* /usr/share/groff/* /usr/share/info/* \
    && find /usr/share/doc -depth -type f ! -name copyright -delete

# Include /usr/local/bin in path.
RUN echo "export PATH=${PATH}:/usr/local/bin >> ~/.bashrc"

# Basic Python tools
RUN pip install --upgrade pip setuptools ipython wheel uwsgi pipdeptree

# NPM
COPY ./scripts/setup-npm.sh /tmp
RUN /tmp/setup-npm.sh

#
# {{ cookiecutter.project_shortname }} specific
#

# Create instance/static folder
ENV INVENIO_INSTANCE_PATH /usr/local/var/instance
RUN mkdir -p ${INVENIO_INSTANCE_PATH}
WORKDIR /tmp

# Copy and install requirements. Faster build utilizing the Docker cache.
COPY requirements*.txt /tmp/
RUN mkdir -p /usr/local/src/ \
    && mkdir -p /code/invenio \
    && pip install -r requirements.txt --src /usr/local/src

# Copy source code
COPY . /code/invenio
WORKDIR /code/invenio

# Install Invenio (with ES5 and PostgreSQL support)
RUN pip install -e .[postgresql,elasticsearch5,all] \
    && python -O -m compileall .

# Install NPM dependencies and build assets.
RUN zenodo npm --pinned-file /code/invenio/package.pinned.json \
    && cd ${INVENIO_INSTANCE_PATH}/static \
    && npm install \
    && cd /code/invenio \
    && invenio collect -v \
    && invenio assets build

RUN adduser --uid 1000 --disabled-password --gecos '' invenio \
    && chown -R invenio:invenio /code ${INVENIO_INSTANCE_PATH}

RUN mkdir -p /usr/local/var/data && \
    chown invenio:invenio /usr/local/var/data -R && \
    mkdir -p /var/log/invenio && \
    chown invenio:invenio /var/log/invenio -R

COPY ./docker/docker-entrypoint.sh /

USER invenio
VOLUME ["/code/invenio"]
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["invenio", "run", "-h", "0.0.0.0"]
