# pull official base image
FROM python:3.8-slim-buster

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

# # install psycopg2
RUN apt-get update \
    && apt-get install postgresql postgresql-contrib libpq-dev python-dev gcc -y

RUN pip install psycopg2

# install dependencies
COPY ./src/requirements.txt .
RUN pip install -r requirements.txt

RUN python -m snips_nlu download es

# copy project
COPY ./src/ .

RUN python manage.py collectstatic --noinput

CMD gunicorn backend.wsgi:application --bind 0.0.0.0:$PORT