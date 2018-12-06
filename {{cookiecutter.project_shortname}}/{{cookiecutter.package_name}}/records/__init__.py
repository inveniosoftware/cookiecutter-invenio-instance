{% include 'misc/header.py' %}

"""{{ cookiecutter.description }}"""

from __future__ import absolute_import, print_function

from .ext import {{ cookiecutter.datamodel_extension_class }}
from .version import __version__

__all__ = ('__version__', '{{ cookiecutter.datamodel_extension_class }}')
