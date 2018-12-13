{% include 'misc/header.rst' %}
Installation
============

First you need to install
`pipenv <https://docs.pipenv.org/install/#installing-pipenv>`_, it will handle
the virtual environment creation for the project in order to sandbox our Python
environment, as well as manage the dependency installation, among other things.

Start all dependent services using docker-compose (this will start {{cookiecutter.database[:-3].title() + cookiecutter.database[-3:].upper()}},
Elasticsearch {{cookiecutter.elasticsearch}}, RabbitMQ and Redis):

.. code-block:: console

    $ docker-compose up -d

.. note::

    Make sure you have `enough virtual memory
    <https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html#docker-cli-run-prod-mode>`_
    for Elasticsearch in Docker:

    .. code-block:: shell

        # Linux
        $ sysctl -w vm.max_map_count=262144

        # macOS
        $ screen ~/Library/Containers/com.docker.docker/Data/com.docker.driver.amd64-linux/tty
        <enter>
        linut00001:~# sysctl -w vm.max_map_count=262144


Next, bootstrap the instance (this will install all Python dependencies and
build all static assets):

Creating an environment
-----------------------

In order to bootstrap and install your instance, it is recommended to use a
virtual environment. For that we will use ``pipenv``.

.. code-block:: console

    $ pipenv shell
    Creating a virtualenv for this project…
    Pipfile: ~/my-site/Pipfile
    Using /usr/bin/python3.6 (3.6.7) to create virtualenv…
    ⠧ Creating virtual environment...Already using interpreter /usr/bin/python3.6
    Using base prefix '/usr'
    New python executable in /venv/my-site-oIVvLp1Q/bin/python3.6
    Also creating executable in /venv/my-site-oIVvLp1Q/bin/python
    Installing setuptools, pip, wheel...
    done.

    ✔ Successfully created virtual environment!
    Virtualenv location: /venv/my-site-oIVvLp1Q
    Creating a Pipfile for this project…
    Launching subshell in virtual environment…
     . /venv/my-site-oIVvLp1Q/bin/activate
    $. /venv/my-site-oIVvLp1Q/bin/activate
    (my-site)$

Note that this will generate a virtual environment with the name of the
folder in which you are at (`my-site` in the example above).

Bootstrapping
-------------

.. code-block:: console

    $ ./scripts/bootstrap

Next, create database tables, search indexes and message queues:

.. code-block:: console

    $ ./scripts/setup

Running
-------
Start the webserver and the celery worker:

.. code-block:: console

    $ ./scripts/server

Start a Python shell:

.. code-block:: console

    $ ./scripts/console

Upgrading
---------
In order to upgrade an existing instance simply run:

.. code-block:: console

    $ ./scripts/update

Testing
-------
Run the test suite via the provided script:

.. code-block:: console

    $ ./run-tests.sh

By default, end-to-end tests are skipped. You can include the E2E tests like
this:

.. code-block:: console

    $ env E2E=yes ./run-tests.sh

For more information about end-to-end testing see `pytest-invenio
<https://pytest-invenio.readthedocs.io/en/latest/usage.html#running-e2e-tests>`_

Documentation
-------------
You can build the documentation with:

.. code-block:: console

    $ pipenv run build_sphinx

Production environment
----------------------
You can use simulate a full production environment using the
``docker-compose.full.yml``. You can start it like this:

.. code-block:: console

    $ docker-compose -f docker-compose.full.yml up -d

In addition to the normal ``docker-compose.yml``, this one will start:

- HAProxy (load balancer)
- Nginx (web frontend)
- uWSGI (application container)
- Celery (background task worker)
- Flower (Celery monitoring)
