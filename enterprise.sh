#!/bin/sh

# Starts the enterprise gunicorn server (no --reload)
echo "Starting api"

if [[ "$CODECOV_WRAPPER" ]]; then
SUB="$CODECOV_WRAPPER"
else
SUB=""
fi
if [[ "$CODECOV_WRAPPER_POST" ]]; then
POST="$CODECOV_WRAPPER_POST"
else
POST=""
fi
statsd=""
if [[ "$STATSD_HOST" ]]; then
  statsd="--statsd-host ${STATSD_HOST}:${STATSD_PORT} "
fi
if [[ "$1" = "api" || -z "$1" ]];
then
  # Migrate
  python manage.py migrate
  # Start api
  ${SUB}$prefix gunicorn codecov.wsgi:application --workers=${GUNICORN_WORKERS:-2} --bind ${CODECOV_API_BIND:-0.0.0.0}:${CODECOV_API_PORT:-8000} --access-logfile '-' ${statsd}--timeout "${GUNICORN_TIMEOUT:-600}"${POST}
elif [[ "$1" = "rti" ]];
then
  # Start api
  ${SUB}$prefix gunicorn codecov.wsgi:application --workers=${GUNICORN_WORKERS:-2} --bind ${CODECOV_API_BIND:-0.0.0.0}:${CODECOV_API_PORT:-8000} --access-logfile '-' ${statsd}--timeout "${GUNICORN_TIMEOUT:-600}"${POST}
elif [[ "$1" = "migrate" ]];
then
  python manage.py migrate
else
  exec "$@"
fi
