#!/bin/bash

if [[ -z "${ENVIRONMENT}" ]]; then
    echo "Running web application: development"
    pyppeteer-install
    python src/manage.py makemigrations
    python src/manage.py migrate
    python src/manage.py runserver 0.0.0.0:8000
elif [[ ${ENVIRONMENT} == "production" ]]; then
    echo "Running web application: production"
    python src/manage.py migrate
    python src/manage.py runserver 0.0.0.0:8000
fi
