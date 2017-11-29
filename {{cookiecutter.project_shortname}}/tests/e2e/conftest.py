{% include 'misc/header.py' %}
"""Pytest configuration for end-to-end tests."""

import os

import pytest
from elasticsearch.exceptions import RequestError
from invenio_app.factory import create_app
from invenio_db import db as db_
from invenio_search import current_search, current_search_client
from selenium import webdriver
from sqlalchemy_utils.functions import create_database, database_exists


@pytest.fixture(scope='session', autouse=True)
def base_app(tmpdir_factory):
    """Flask application fixture for E2E/integration/selenium tests."""
    tmpdir = tmpdir_factory.mktemp('data')
    sqlite = 'sqlite:///{filepath}'.format(filepath=tmpdir.join('test.db'))

    os.environ.update(
        APP_INSTANCE_PATH=os.environ.get('INSTANCE_PATH', str(tmpdir))
    )

    app_ = create_app(
        DEBUG_TB_ENABLED=False,
        SQLALCHEMY_DATABASE_URI=os.environ.get(
            'SQLALCHEMY_DATABASE_URI',
            sqlite),
        SECRET_KEY="CHANGE_ME",
        SECURITY_PASSWORD_SALT="CHANGE_ME",
        TESTING=True,
        DEBUG=True,
    )

    with app_.app_context():
        yield app_


@pytest.fixture(scope='session')
def es(base_app):
    """Provide elasticsearch access."""
    try:
        list(current_search.create())
    except RequestError:
        list(current_search.delete())
        list(current_search.create())
    current_search_client.indices.refresh()

    yield current_search_client

    list(current_search.delete(ignore=[404]))


@pytest.fixture(scope='session')
def db(base_app):
    """Setup database."""
    if not database_exists(str(db_.engine.url)):
        create_database(str(db_.engine.url))
    db_.create_all()

    yield db_

    db_.session.remove()
    db_.drop_all()


@pytest.fixture
def app(base_app, es, db):
    """Application with ES and DB."""
    yield app


def pytest_generate_tests(metafunc):
    """Override pytest's default test collection function.

    Check if the E2E is set and its value to determine if the end-to-end
    tests need to be executed.

    For each test in this directory which uses the `env_browser` fixture,
    the given test is called once for each value found in the
    `E2E_WEBDRIVER_BROWSERS` environment variable.
    """
    if os.environ.get('E2E', 'no') != 'yes':
        pytest.skip("E2E env var set to 'no', end-to-end tests skipped")

    if 'env_browser' in metafunc.fixturenames:
        browsers = os.environ.get('E2E_WEBDRIVER_BROWSERS',
                                  'Chrome').split()
        metafunc.parametrize('env_browser', browsers, indirect=True)


@pytest.fixture
def browser(request):
    """Fixture for a webdriver instance of the browser."""
    browser_name = getattr(request, 'param', 'Chrome')
    driver = getattr(webdriver, browser_name)()

    yield driver

    _take_screenshot_if_test_failed(driver, request)
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Add hook to track if the test passed or failed."""
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)


def _take_screenshot_if_test_failed(driver, request):
    """Take a screenshot if the test failed."""
    if request.node.rep_call.failed:
        from datetime import datetime
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = 'screenshot-{now}.png'.format(now=now)
        filepath = os.path.join(_get_screenshots_dir(), filename)
        driver.get_screenshot_as_file(filepath)
        base64_screenshot = driver.get_screenshot_as_base64()
        print("Base64 screenshot of failing test: %s" % base64_screenshot)


def _get_screenshots_dir():
    """Create the screenshots directory."""
    directory = ".e2e_screenshots"
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory
