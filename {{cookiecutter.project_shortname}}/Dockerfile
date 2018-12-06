{% include 'misc/header.py' %}
FROM {{cookiecutter.project_shortname}}-base:latest

COPY ./ .

RUN pip install --user .

RUN pipenv run invenio collect -v
RUN pipenv run invenio webpack buildall
