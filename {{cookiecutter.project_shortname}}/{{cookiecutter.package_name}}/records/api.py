{% include 'misc/header.py' %}
"""Records API."""

from __future__ import absolute_import, print_function

from invenio_records_files.api import Record as FilesRecord


class Record(FilesRecord):
    """Custom record."""

    _schema = "records/record-v1.0.0.json"
