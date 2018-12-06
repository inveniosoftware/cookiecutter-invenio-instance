#!/usr/bin/env sh

echo "-------------------------------------------------------------------------------"
echo
echo "Generating SSL certificate and private key for testing...."

openssl req -x509 -newkey rsa:4096 -nodes -out docker/nginx/test.crt -keyout docker/nginx/test.key -days 365 -subj "/C=CH/ST=./L=./O=./OU=./CN=localhost/emailAddress=."
cat docker/nginx/test.crt docker/nginx/test.key > docker/haproxy/haproxy_cert.pem

echo "-------------------------------------------------------------------------------"
echo
echo "Skeleton generated."

echo "Please fix the following TODOs before you use the generated files:"
grep --color=always --recursive --context=3 --line-number TODO .

{%- if cookiecutter.datamodel == 'None' %}
rm -r {{ cookiecutter.package_name }}/records
rm -r tests/api/test_api_simple_flow.py
{%- endif %}

rm -r misc/
