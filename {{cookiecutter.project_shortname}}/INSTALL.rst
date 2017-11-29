Installation
============

Update npm and install a few global packages:

.. code-block:: console

    $ npm update && npm install --silent -g node-sass@3.8.0 clean-css@3.4.19 uglify-js@2.7.3 requirejs@2.2.0

Upgrade pip, setuptools and wheel to make sure you have latest versions:

.. code-block:: console

    $ mkvirtualenv ils
    (ils)$ pip install --upgrade pip setuptools wheel

Install {{cookiecutter.project_name}}:

.. code-block:: console

   (ils)$ pip install {{cookiecutter.project_shortname}}[postgresql,elasticsearch2]

Install web assets (JavaScript and CSS dependencies):

.. code-block:: console

   (ils)$ invenio npm
   (ils)$ cdvirtualenv var/instance/static/
   (ils)$ npm install

Build web assets and collect static files:

.. code-block:: console

   (ils)$ invenio collect -v
   (ils)$ invenio assets build

Configuration
-------------
Next, you need to configure Invenio to tell where it can find your SQL
database, Redis cache, RabbitMQ message broker and Elasticsearch search engine:

The configuration file is located in:

- ``<sys.prefix>/var/instance/invenio.cfg``

In the examples below we assume the remote services are running on the IP
address ``192.168.33.3``.

.. note::

    If you have everything running ``localhost`` without passwords, you can skip
    the configuration as everything is pre-configured for ``localhost``.

Invenio
~~~~~~~
The most important Invenio related configuration to set is:

.. code-block:: python

    SECRET_KEY = '...your-very-secret-key...'

The secret key is used for protecting sessions and encrypting/decrypting
tokens. For production systems is critical to set this configuration to keep
your system secure.

Database
~~~~~~~~
Next, you need to tell  Invenio which database you want to use. By default for
development purposes, Invenio will create a SQLite database next to
``invenio.cfg``. To configure Invenio to use e.g. PostgreSQL set the following
configuration:

.. code-block:: python

    SQLALCHEMY_DATABASE_URI='postgresql://invenio:invenio@192.168.33.3/invenio'

Search engine
~~~~~~~~~~~~~
Next, point Invenio to your Elasticsearch cluster:

.. code-block:: python

    SEARCH_ELASTIC_HOSTS=['192.168.33.3:9200']

Message broker
~~~~~~~~~~~~~~
Next, configure where Invenio can find the RabbitMQ message broker used for
background jobs and bulk indexing:

.. code-block:: python

    CELERY_BROKER_URL='amqp://invenio:invenio@192.168.33.3:5672/invenio'


Cache
~~~~~
Last, you need to configure where Invenio can find the Redis cache. The cache
needs to be set in a couple of variables, as it is being used for different
purposes (e.g. session store, background job results, caching):

.. code-block:: python

    CACHE_TYPE='redis'
    CACHE_REDIS_URL='redis://192.168.33.3:6379/0'
    ACCOUNTS_SESSION_REDIS_URL='redis://192.168.33.3:6379/1'
    CELERY_RESULT_BACKEND='redis://192.168.33.3:6379/2'

Note, that each variable above points to a different database number in Redis
(the ``0``, ``1``, ``2`` suffix in the URL)

Database and search index
-------------------------
The last you need to do is to create the database tables and search indexes.

Create the database (not needed if the database was created outside of invenio
already):

.. code-block:: console

   (ils)$ invenio db init

Create the database tables:

.. code-block:: console

   (ils)$ invenio db create

Create the search indexes and indexing queue:

.. code-block:: console

    (ils)$ invenio index init
    (ils)$ invenio index queue init


.. note::

    If for some reason something failed during table or index creation, you
    can remove everything again with:

    .. code-block:: console

        (ils)$ invenio db drop --yes-i-know
        (ils)$ invenio index destroy --force
