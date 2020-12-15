{% include 'misc/header.py' %}

"""{{ cookiecutter.description }}"""

from .ext import {{ cookiecutter.datamodel_extension_class }}

__all__ = ('{{ cookiecutter.datamodel_extension_class }}', )
