FROM haproxy:1.5
RUN mkdir -p /usr/local/var/lib/haproxy/
COPY haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg
COPY haproxy_cert.pem /usr/local/etc/cert.pem
