#!/bin/bash
docker exec -ti -u root carepanel-app python manage.py makemigrations
