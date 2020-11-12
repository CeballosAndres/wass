FROM python:3
RUN mkdir /code
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN chmod 777 /code/app/runner.sh
# ENV PORT=8000
EXPOSE 8000

CMD /code/app/runner.sh
