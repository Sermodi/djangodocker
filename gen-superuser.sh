#!/bin/bash
docker-compose run --rm carepanel-app python manage.py createsuperuser
