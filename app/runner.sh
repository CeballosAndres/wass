#!/bin/bash
python manage.py migrate
python manage.py collectstatic --noinput
# python manage.py crontab remove
/etc/init.d/cron start
python manage.py crontab add
gunicorn --bind "0.0.0.0:${PORT}" app.wsgi