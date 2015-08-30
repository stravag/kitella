# kitella

FIXME

## Prerequisites

You will need [Leiningen][] 2.0.0 or above installed.

[leiningen]: https://github.com/technomancy/leiningen

## Running

To start a web server for the application, run:

    lein ring server

## License

Copyright © 2015 FIXME

### Setup DB

Run in REPL:

```
(require '[clojure.java.jdbc :as sql])
(sql/with-connection
  {:classname "org.h2.Driver"
   :subprotocol "h2:file"
   :subname "db/kitella"}

  (sql/create-table :locations
    [:id "bigint primary key auto_increment"]
    [:x "integer"]
    [:y "integer"])

  (sql/insert-records :locations
    {:x 8 :y 9}))
 ```