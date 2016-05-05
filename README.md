# kitella

FIXME

## Prerequisites

You will need [Leiningen][] 2.0.0 or above installed.

[leiningen]: https://github.com/technomancy/leiningen

## Reference

https://devcenter.heroku.com/articles/clojure-web-application

## Setup/Run Database

Rather than running PostgreSQL as a system-level background
daemon as some package managers do by default, it’s recommended
for development work that you launch postgres yourself to avoid
permissions issues and improve visibility:

    $ initdb pg
    $ postgres -D pg

Then create a local PostgreSQL database for development work:

    $ createdb kitella

### Database initialization / migration

    $ lein migrate

## Running Application

To start a web server for the application, run:

    $ lein ring server