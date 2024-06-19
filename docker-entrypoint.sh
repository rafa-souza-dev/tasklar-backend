#!/bin/bash

echo "Waiting for mysql..."
while ! nc -z $DB_HOST $DB_PORT; do
    sleep 0.1
done
echo "MySQL started"

echo "Appling database migrations..."
python manage.py makemigrations 
python manage.py migrate

exec "$@"
