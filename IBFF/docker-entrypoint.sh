#!/bin/sh

ADMIN="admin"
ADMIN_PASSWORD="admin"
ADMIN_EMAIL="admin@admin.com"

venv/bin/python manage.py makemigrations
venv/bin/python manage.py migrate

export DJANGO_SUPERUSER_USERNAME=$ADMIN
export DJANGO_SUPERUSER_PASSWORD=$ADMIN_PASSWORD
export DJANGO_SUPERUSER_EMAIL=$ADMIN_EMAIL
venv/bin/python manage.py createsuperuser --noinput

venv/bin/python manage.py runserver "0.0.0.0:8000"
