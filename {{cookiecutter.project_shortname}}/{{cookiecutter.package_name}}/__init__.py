{% include 'misc/header.py' %}
"""{{cookiecutter.project_name}}.

Running
-------
Starting a development server is as simple as:

.. code-block:: console

    $ export FLASK_DEBUG=1
    $ invenio run


.. note::

   You must enable the debug mode as done above to prevent that all
   connections are forced to HTTPS since the development server does not work
   with HTTPS.

Celery workers can be started using the command:

.. code-block:: console

    $ celery worker -A invenio_app.celery -l INFO

An interactive Python shell is started with the command:

.. code-block:: console

    $ invenio shell
"""

from __future__ import absolute_import, print_function

from .version import __version__

__all__ = ('__version__', )
