..
    This file is part of Invenio.
    Copyright (C) 2015-2018 CERN.

    Invenio is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.

==============================
 Cookiecutter-Invenio-Instance
==============================

.. image:: https://img.shields.io/github/license/inveniosoftware/cookiecutter-invenio-instance.svg
        :target: https://github.com/inveniosoftware/cookiecutter-invenio-instance/blob/master/LICENSE

.. image:: https://img.shields.io/travis/inveniosoftware/cookiecutter-invenio-instance.svg
        :target: https://travis-ci.org/inveniosoftware/cookiecutter-invenio-instance

This `Cookiecutter <https://github.com/audreyr/cookiecutter>`_ template is
designed to help you to bootstrap an `Invenio
<https://github.com/inveniosoftware/invenio>`_ service.

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet::

    pip install -U cookiecutter

Generate your Invenio instance::

    cookiecutter https://github.com/inveniosoftware/cookiecutter-invenio-instance.git -c v3.1

More detailed steps can be found in the https://inveniosoftware.org/#getstarted

Features
--------

- **Python package:** Python package for your service.
- **Boilerplate files:** `README` including important badges, `AUTHORS` and
  `CHANGES` files.
- **License:** `MIT <https://opensource.org/licenses/MIT>`_ file and headers.
- **Installation:** Installation workflow and dependency management using
  `pipenv <https://docs.pipenv.org/:>`_.
- **Tests:** Testing setup using `pytest <http://pytest.org/latest/>`_.
- **Documentation:** Documentation generator using `Sphinx
  <http://sphinx-doc.org/>`_. Also includes all files required for `Read the
  Docs <https://readthedocs.io/>`_. Mocking module to simulate not-installed
  requirements for faster documentation building.
- **Continuous integration:** Support for `Travis <https://travis-ci.org/>`_
  which tests all requirement levels and adds coverage tests using `Coveralls
  <https://coveralls.io/>`_.
- **Your toolchain:** Ignores a decent set of files when working with Git and
  `Docker <https://www.docker.com/>`_. Gets your editor to adapt project
  guidelines by providing an `EditorConfig <http://editorconfig.org/>`_ file.

Configuration
-------------
To generate correct files, please provide the following input to Cookiecutter:

============================ ==============================================================
`project_name`                Full project name, might contain spaces.
`project_shortname`           Project shortname, no spaces allowed, use `-` as a
                              separator.
`project_site`                Project website host.
`package_name`                Package/Module name for Python, must follow `PEP 0008
                              <https://www.python.org/dev/peps/pep-0008/>`_.
`github_repo`                 GitHub repository of the project in form of `USER/REPO`,
                              not the full GitHub URL.
`description`                 A short description of the functionality of the module,
                              its length should not extend one line.
`author_name`                 The name of the primary author of the project, not
                              necessarily the same as the copyright holder.
`author_email`                E-Mail address of the primary author.
`year`                        Current year.
`copyright_holder`            Name of the person or organization who acts as the
                              copyright holder of this project.
`transifex_project`           Name of the project on transifex translation platform.
`database`                    The database you are planning to use. PostgreSQL
                              (`postgresql`) and MySQL (`mysql`) supported at the
                              moment.
`elasticsearch`               The version of ElasticSearch you are planning to use.
                              Versions 6.x (`elasticsearch6`) and 7.x (`elasticsearch7`)
                              supported at the moment.
`datamodel`                   Whether to create a custom model (`Custom`) or continue
                              without one (`None`).
`datamodel_extension_class`   Name of the class of your custom datamodel.
`datamodel_pid_name`          Name of the Persistent IDentifier attribute of the datamodel.
============================ ==============================================================

Further documentation is available on https://invenio.readthedocs.io/
