FROM python:3.7-slim-buster

ARG DEBIAN_FRONTEND=noninteractive

WORKDIR /opt/asana_control/

RUN DEBIAN_FRONTEND=noninteractive \
    export PYTHONPATH=/opt/asana_control/

RUN pip3 install --no-cache-dir psycopg2-binary==2.8.5 requests==2.23.0 asana==0.10.0  && \
	pip3 install --no-cache-dir Django==3.0.6 django-ipware==2.1.0 && \
	pip3 install --no-cache-dir gevent==1.4.0 gunicorn==20.0.4

COPY asana_models asana_models
COPY asana_control asana_control
COPY django_commander django_commander
COPY static static
COPY manage.py ./