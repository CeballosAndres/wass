#!/bin/bash
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn --bind "0.0.0.0:${PORT}" app.wsgi