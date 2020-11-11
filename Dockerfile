FROM python:3-alpine
ADD . /app
WORKDIR /app
# You will need this if you need PostgreSQL, otherwise just skip this
# RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev
RUN pip install uwsgi
RUN pip install -r requirements.txt
ENV PORT=8000
EXPOSE 8000
# Runner script here
CMD ["/app/runner.sh"]