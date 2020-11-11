#!/usr/bin/env sh
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app.wsgi"]
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn --bind 0.0.0.0:8000 app.wsgi