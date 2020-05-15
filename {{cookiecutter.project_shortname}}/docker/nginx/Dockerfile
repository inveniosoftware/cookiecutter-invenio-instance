{% include 'misc/header.py' %}
{%- if cookiecutter.docker_size == 'light'%}
FROM nginx:alpine
{%- else %}
FROM nginx
{%- endif %}
COPY nginx.conf /etc/nginx/nginx.conf
COPY conf.d/* /etc/nginx/conf.d/
COPY test.key /etc/ssl/private/test.key
COPY test.crt /etc/ssl/certs/test.crt
