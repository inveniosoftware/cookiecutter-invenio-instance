{% include 'misc/header.py' %}
"""Blueprint definitions."""

from __future__ import absolute_import, print_function

from operator import itemgetter
from os.path import splitext

from flask import Blueprint
from invenio_previewer.proxies import current_previewer

blueprint = Blueprint(
    '{{ cookiecutter.package_name}}_records',
    __name__,
    template_folder='templates',
    static_folder='static',
)
"""Blueprint used for loading templates and static assets

The sole purpose of this blueprint is to ensure that Invenio can find the
templates and static files located in the folders of the same names next to
this file.
"""


#
# Files related template filters.
#
@blueprint.app_template_filter()
def select_preview_file(files):
    """Get list of files and select one for preview."""
    selected = None

    try:
        for f in sorted(files or [], key=itemgetter('key')):
            file_type = splitext(f['key'])[1][1:].lower()
            if file_type in current_previewer.previewable_extensions:
                if selected is None:
                    selected = f
                elif f['default']:
                    selected = f
    except KeyError:
        pass
    return selected
