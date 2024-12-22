#!/bin/bash
set -e  # Exit on error

echo "Starting deployment script..."
cd /home/site/wwwroot

echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Running migrations..."
python manage.py migrate --noinput

echo "Starting Gunicorn..."
gunicorn --bind=0.0.0.0:8000 --workers=2 --threads=4 --timeout=120 backend.wsgi:application
