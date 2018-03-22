Installation
============

You can install ``{{cookiecutter.project_name}}`` and each service (database, Elasticsearch, etc.) in your machine
or you can use ``docker-compose`` to run it in one command.
The easiest way to run Invenio is by using Docker. For a complete installation and usage guide, please refer to
the `Invenio documentation <https://invenio.readthedocs.io/en/latest/usersguide/>`.

Quick start
-----------

.. note::

    The docker configuration provided in this module uses PostgresSQL and ElasticSearch 6. If you have chosen different
    database or ElasticSearch version and you want to try this quick start with Docker, modify the ``setup.py``
    configuration.

Install `Docker` and ``docker-compose`` in your machine.
Then, create and run all the docker containers:

.. code-block:: console

    $ cd {{ cookiecutter.project_shortname }}
    $ docker-compose -f docker-compose.full.yml up

Database and search index
-------------------------
The last you need to do is to create the database tables and search indexes.
Connect to the web container:

.. code-block:: console

    $ docker run -it {{ cookiecutter.project_shortname }}-web-ui /bin/bash

Run the following commands inside the docker container.
Create the database and tables:

.. code-block:: console

   $ {{ cookiecutter.project_shortname }} db init create

Create the search indexes and indexing queue:

.. code-block:: console

    $ {{ cookiecutter.project_shortname }} index init
    $ {{ cookiecutter.project_shortname }} index queue init

Open your browser and visit the url https://localhost.

.. note::

    If for some reason something failed during table or index creation, you
    can remove everything again with:

    .. code-block:: console

        $ {{ cookiecutter.project_shortname }} db drop --yes-i-know
        $ {{ cookiecutter.project_shortname }} index destroy --force

Development setup
-----------------

The recommended way of developing on Invenio is to install and run the web app locally in your machine, while keeping
the other services (provided by `docker-compose.yml`) on Docker containers.
See the `Developer Guide <https://http://invenio.readthedocs.io/en/latest/developersguide/>` documentation.
