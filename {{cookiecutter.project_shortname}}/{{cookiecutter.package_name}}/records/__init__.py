{% include 'misc/header.py' %}

"""{{ cookiecutter.description }}"""

from __future__ import absolute_import, print_function

from .ext import {{ cookiecutter.datamodel_extension_class }}

__all__ = ('{{ cookiecutter.datamodel_extension_class }}', )
