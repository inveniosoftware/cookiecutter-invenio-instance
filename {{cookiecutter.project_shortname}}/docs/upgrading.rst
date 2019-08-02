{% include 'misc/header.rst' %}

Upgrading to version 3.2
========================

If you have your instance of Invenio v3.1 already up and running and
 you would like to upgrade to version v3.2 you don't need to set up your
 project from a scratch. The goal of this guide is to show the steps to upgrade
 your project without loosing any of your work.


Pipfile modifications
---------------------

Most important changes that you will have to make are in Pipfile

First you need to change the invenio version:
.. code-block::

   invenio = { version = "==3.2.0a3", extras = ["base", "auth", "metadata", "files", "{{ cookiecutter.database }}", "elasticsearch{{ cookiecutter.elasticsearch }}" ]}



Elasticsearch upgrades
----------------------
Alongside with Invenio v3.2 comes compatibility with elasticsearch 7.x
To change it... # TODO


Permissions
-----------
