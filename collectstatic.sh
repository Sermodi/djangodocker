#!/bin/bash
docker exec -ti vineabot-app python manage.py collectstatic
