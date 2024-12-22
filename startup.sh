#!/bin/bash

# Move to the correct directory
cd /home/site/wwwroot

# Install dependencies
pip install -r requirements.txt

# Django commands
python manage.py collectstatic --noinput
python manage.py migrate

# Start Gunicorn
exec gunicorn --bind=0.0.0.0:8000 --timeout 600 backend.wsgi:application
