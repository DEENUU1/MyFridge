FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./myfridge/myfridge/requirements.txt /app/

RUN pip install -r requirements.txt

COPY ./myfridge/myfridge /app/
