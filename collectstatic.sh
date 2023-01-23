#!/bin/bash
docker exec -ti {APPName} python manage.py collectstatic
