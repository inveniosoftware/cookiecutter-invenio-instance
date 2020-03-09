{% include 'misc/header.py' %}
"""Test record and files."""

import json

from invenio_search import current_search
from six import BytesIO


def _create_record(client):
    """Create record."""
    headers = [("Content-Type", "application/json")]
    data = {
            "title": "The title of the record ",
            "contributors": [
                {"name": "Ellis Jonathan"},
            ]
        }
    url = "https://localhost:5000/records/"
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 201
    current_search.flush_and_refresh("records")

    rec = response.get_json()
    pid_value = rec["id"]
    return pid_value, rec


def _get_record(client, pid_value):
    """Get record by PID."""
    url = "https://localhost:5000/records/{}".format(pid_value)
    response = client.get(url)
    assert response.status_code == 200
    rec = response.get_json()
    return rec


def test_record_creation(client, location):
    """Test create record using REST API."""
    pid_value, rec = _create_record(client)
    assert "_bucket" not in rec
    assert "files" not in rec
    assert "$schema" not in rec['metadata']

    # retrieve record
    rec = _get_record(client, pid_value)
    assert "_bucket" not in rec
    assert "files" not in rec
    assert "$schema" not in rec['metadata']


def test_files_creation_deletion(client, location):
    """Test that files are in record metadata."""
    pid_value, _ = _create_record(client)

    # add a file
    headers = [("Content-Type", "application/octet-stream")]
    data = BytesIO(b"my file contents")
    url = "https://localhost:5000/records/{}/files/test.jpg".format(pid_value)
    response = client.put(url, input_stream=data, headers=headers)
    assert response.status_code == 200

    # retrieve record and files
    rec = _get_record(client, pid_value)
    assert "_bucket" not in rec
    assert "files" in rec
    first_file = rec["files"][0]
    first_file["key"] = "test.jpg"

    # Check if the files link is present
    files_link = 'https://localhost:5000/records/1/files'
    assert rec['links']['files'] == files_link

    # delete file
    headers = [("Content-Type", "application/octet-stream")]
    url = "https://localhost:5000/records/{}/files/test.jpg".format(pid_value)
    response = client.delete(url, headers=headers)
    assert response.status_code == 204

    # retrieve record and files
    rec = _get_record(client, pid_value)
    assert "_bucket" not in rec
    assert rec["files"] == []
