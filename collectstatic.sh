#!/bin/bash
docker exec -ti carepanel-app python manage.py collectstatic
