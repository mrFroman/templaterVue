#! /bin/bash

python backend\manage.py makemigrations --no-input
python backend\manage.py migrate --no-input

python backend\manage.py collectstatic --no-input

exec gunicorn calculator.wsgi:application -b 0.0.0.0:8000 --reload