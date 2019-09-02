{% include 'misc/header.py' %}
{%- if cookiecutter.docker_size == 'light'%}
FROM haproxy:1.8-alpine
{%- else %}
FROM haproxy:1.8
{%- endif %}
RUN mkdir -p /usr/local/var/lib/haproxy/
COPY haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg
COPY haproxy_cert.pem /usr/local/etc/cert.pem
