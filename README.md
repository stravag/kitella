# kitella

FIXME

## Prerequisites

### Python / Django

Install pyhton3: https://www.python.org/downloads/

Install django & postgres adapter

    pip3 install django
    pip3 install psycopg2

### Database setup

Initialize Postgres

    initdb --username=postgres --pwprompt db

Start Postgres

    postgres -D db

Create kitella database

    createdb --username=postgres kitella

Migration

    python3 manage.py migrate

## Running

To start a web server for the application, run:

    python3 manage.py runserver

## Development

Create new migrations when models have changed

    python3 manage.py makemigrations <app-name>
