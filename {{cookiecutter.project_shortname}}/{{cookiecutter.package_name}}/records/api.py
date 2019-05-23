{% include 'misc/header.py' %}
"""Invenio-Records-Files API."""

from __future__ import absolute_import, print_function

from invenio_records_files.api import Record, FilesMixin
from invenio_db import db
from invenio_files_rest.models import Bucket


class RecordWithBucket(Record, FilesMixin):

    def _create_bucket(self):
        bucket = Bucket.create()
        db.session.commit()
        return bucket
