{% include 'misc/header.py' %}
"""E2E integration tests."""

from flask import url_for


def test_frontpage(live_server, browser):
    """Test retrieval of front page."""
    browser.get(url_for('invenio_theme_frontpage.index', _external=True))
    assert "{{cookiecutter.project_name}}" == browser.find_element_by_xpath(
        "//div[contains(@class, 'frontpage-search')]/*/h1").text
