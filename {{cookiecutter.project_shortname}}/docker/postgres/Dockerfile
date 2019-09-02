{% include 'misc/header.py' %}
{%- if cookiecutter.docker_size == 'light'%}
FROM postgres:9.6-alpine
{%- else %}
FROM postgres:9.6
{%- endif %}
COPY ./init-app-db.sh /docker-entrypoint-initdb.d/10-init-app-db.sh
