# pull official base image
FROM python:3.11-alpine
# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev \
    && apk add --no-cache python3-dev openssl-dev libffi-dev gcc

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements/local/requirements.txt .
RUN pip install -r requirements.txt

# Run the service
CMD python manage.py migrate \
    && python manage.py runserver 0.0.0.0:8000
