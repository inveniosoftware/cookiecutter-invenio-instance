{% include 'misc/header.py' %}
"""Default configuration for {{cookiecutter.project_name}}."""

from __future__ import absolute_import, print_function

from datetime import timedelta

from invenio_app.config import APP_DEFAULT_SECURE_HEADERS


def _(x):
    """Identity function used to trigger string extraction."""
    return x


# I18N
# ====
#: Default language
BABEL_DEFAULT_LANGUAGE = 'en'
#: Default time zone
BABEL_DEFAULT_TIMEZONE = 'Europe/Zurich'
#: Other supported languages (do not include default language in list).
I18N_LANGUAGES = [
    ('fr', _('French'))
]


# Base templates
# ==============
#: Global base template.
BASE_TEMPLATE = 'invenio_theme/page.html'
#: Cover page base template (used for e.g. login/sign-up).
COVER_TEMPLATE = 'invenio_theme/page_cover.html'
#: Footer base template.
FOOTER_TEMPLATE = 'invenio_theme/footer.html'
#: Header base template.
HEADER_TEMPLATE = 'invenio_theme/header.html'
#: Settings base template.
SETTINGS_TEMPLATE = 'invenio_theme/page_settings.html'


# Theme configuration
# ===================
#: Site name
THEME_SITENAME = _('{{cookiecutter.project_name}}')
#: Use default frontpage.
THEME_FRONTPAGE = True
#: Frontpage title.
THEME_FRONTPAGE_TITLE = _('{{cookiecutter.project_name}}')
#: Frontpage template.
THEME_FRONTPAGE_TEMPLATE = '{{cookiecutter.package_name}}/frontpage.html'


# Email configuration
# ===================
#: Email address for support.
SUPPORT_EMAIL = "{{ cookiecutter.author_email }}"
#: Disable email sending by default.
MAIL_SUPPRESS_SEND = True

# Assets
# ======
#: Static files collection method (defaults to copying files).
COLLECT_STORAGE = 'flask_collect.storage.file'

# Accounts
# ========
SECURITY_EMAIL_SENDER = SUPPORT_EMAIL
SECURITY_EMAIL_SUBJECT_REGISTER = _(
    "Welcome to {{cookiecutter.project_name}}!")

# Celery configuration
# ====================
#: Scheduled tasks configuration (aka cronjobs).
CELERY_BEAT_SCHEDULE = {
    'indexer': {
        'task': 'invenio_indexer.tasks.process_bulk_queue',
        'schedule': timedelta(minutes=5),
    },
    'accounts': {
        'task': 'invenio_accounts.tasks.clean_session_table',
        'schedule': timedelta(minutes=60),
    },
}

# Flask configuration
# ===================
# See details on
# http://flask.pocoo.org/docs/0.12/config/#builtin-configuration-values

#: Max upload size for form data via application/mulitpart-formdata
MAX_CONTENT_LENGTH = 100 * 1024 * 1024  # 100 MiB

# REST
# ====
#: Enable Cross-Origin Resource Sharing support.
REST_ENABLE_CORS = True

APP_DEFAULT_SECURE_HEADERS['force_https'] = False
APP_DEFAULT_SECURE_HEADERS['session_cookie_secure'] = False

# Debug
# =====
# Flask-DebugToolbar is by default enabled when the application is running in
# debug mode. More configuration options are available at
# https://flask-debugtoolbar.readthedocs.io/en/latest/#configuration

#: Switches off incept of redirects by Flask-DebugToolbar.
DEBUG_TB_INTERCEPT_REDIRECTS = False
