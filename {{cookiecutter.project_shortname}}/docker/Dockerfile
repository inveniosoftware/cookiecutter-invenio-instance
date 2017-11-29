FROM centos:7

# Install pre-requisites:
RUN yum update -y && \
    yum install -y \
        curl \
        git \
        rlwrap \
        screen \
        vim \
        emacs-nox && \
    yum install -y \
        epel-release && \
    yum groupinstall -y "Development Tools" && \
    yum install -y \
        libffi-devel \
        libxml2-devel \
        libxslt-devel \
        npm \
        python-devel \
        python-pip

# Install xrootd and dependencies if needed
ARG XROOTD=False
RUN if [ -z "$XROOTD" ]; then \
        yum install -y \
            expect \
            policycoreutils \
            selinux-policy && \
        rpm -Uvh \
            http://xrootd.web.cern.ch/xrootd/sw/releases/4.7.1/rpms/user_xrootd/slc7/x86_64/xrootd-libs-4.7.1-1.el7.x86_64.rpm \
            http://xrootd.web.cern.ch/xrootd/sw/releases/4.7.1/rpms/user_xrootd/slc7/x86_64/xrootd-server-libs-4.7.1-1.el7.x86_64.rpm \
            http://xrootd.web.cern.ch/xrootd/sw/releases/4.7.1/rpms/user_xrootd/slc7/x86_64/xrootd-server-4.7.1-1.el7.x86_64.rpm \
            http://xrootd.web.cern.ch/xrootd/sw/releases/4.7.1/rpms/user_xrootd/slc7/x86_64/xrootd-selinux-4.7.1-1.el7.noarch.rpm \
            http://xrootd.web.cern.ch/xrootd/sw/releases/4.7.1/rpms/user_xrootd/slc7/x86_64/xrootd-client-devel-4.7.1-1.el7.x86_64.rpm \
            http://xrootd.web.cern.ch/xrootd/sw/releases/4.7.1/rpms/user_xrootd/slc7/x86_64/xrootd-client-4.7.1-1.el7.x86_64.rpm \
            http://xrootd.web.cern.ch/xrootd/sw/releases/4.7.1/rpms/user_xrootd/slc7/x86_64/xrootd-client-libs-4.7.1-1.el7.x86_64.rpm \
            http://xrootd.web.cern.ch/xrootd/sw/releases/4.7.1/rpms/user_xrootd/slc7/x86_64/xrootd-devel-4.7.1-1.el7.x86_64.rpm \
            http://xrootd.web.cern.ch/xrootd/sw/releases/4.7.1/rpms/user_xrootd/slc7/x86_64/xrootd-4.7.1-1.el7.x86_64.rpm \
            http://xrootd.web.cern.ch/xrootd/sw/releases/4.7.1/rpms/user_xrootd/slc7/x86_64/xrootd-python-4.7.1-1.el7.x86_64.rpm; \
    fi;

RUN yum clean -y all

RUN pip install --upgrade pip setuptools wheel && \
    npm update && \
    npm install --silent -g node-sass@3.8.0 clean-css@3.4.24 uglify-js requirejs

RUN python -m site
RUN python -m site --user-site

# Install Invenio
ENV WORKING_DIR=/opt/{{cookiecutter.project_shortname}}
ENV INVENIO_INSTANCE_PATH=${WORKING_DIR}/var/instance

# copy everything inside /src
RUN mkdir -p ${WORKING_DIR}/src
COPY ./invenio-app-ils ${WORKING_DIR}/src
WORKDIR ${WORKING_DIR}/src

RUN mkdir -p ${INVENIO_INSTANCE_PATH}

# Install Python dependencies
ARG ENVIRONMENT=DEV
RUN if [ "$ENVIRONMENT" = "DEV" ]; then pip install .[all,postgresql,elasticsearch2]; fi;
RUN if [ "$ENVIRONMENT" = "PROD" ]; then pip install -r requirements.txt; fi;

# Install/create static files
RUN invenio npm && \
    cd ${INVENIO_INSTANCE_PATH}/static && \
    npm install && \
    invenio collect -v && \
    invenio assets build

# copy uwsgi config file
COPY ./uwsgi ${INVENIO_INSTANCE_PATH}
RUN ls -alh ${INVENIO_INSTANCE_PATH}/
RUN ls -alh ${INVENIO_INSTANCE_PATH}/uwsgi.ini

# Set folder permissions
RUN chgrp -R 0 ${INVENIO_INSTANCE_PATH} && \
    chmod -R g=u ${INVENIO_INSTANCE_PATH}

RUN adduser --uid 1000 invenio --gid 0 && \
    chown -R invenio:root ${INVENIO_INSTANCE_PATH}
USER 1000
