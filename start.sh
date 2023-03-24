#!/bin/bash

# Start gunicorn in the background
gunicorn -c /app/gunicorn.conf backend.wsgi:application &

# Start nginx in the foreground
nginx -g "daemon off;"
