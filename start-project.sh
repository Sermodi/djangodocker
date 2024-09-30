#!/bin/bash
if [ $# -eq 0 ]
    then
        echo -e "No me has dicho como se llama el proyecto\n"
else
    docker-compose run --rm vineabot-app django-admin startproject $1
fi
