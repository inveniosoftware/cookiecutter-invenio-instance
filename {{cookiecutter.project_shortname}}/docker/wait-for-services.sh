#!/usr/bin/env bash
{% include 'misc/header.py' %}

RETRIES=5

# Use only one loop and try all services
{%- if cookiecutter.database == 'postgresql'%}
# TODO as with for redis-cli
{%- elif cookiecutter.database == 'mysql'%}
# TODO as with for redis-cli
{%- endif %}
RETRIES=5

while ! $(curl --silent --output /dev/null http://localhost:9200/) = 200; do
  echo 'Waiting for Elasticsearch, $((RETRIES--)) remaining attempts...'
  sleep 2
  if [ $RETRIES -eq 0 ]
  then
    echo "Couldn't reach Elasticsearch"
    exit 1
  fi
done

while ! $(docker-compose exec cache bash -c "redis-cli ping") == 'PONG'; do

done

# Install on travis
# TODO wait for Redis and RabbitMQ
