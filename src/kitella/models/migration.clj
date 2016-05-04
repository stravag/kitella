(ns kitella.models.migration
  (:require [ragtime.jdbc :as jdbc]
            [ragtime.repl :as repl]))

(def config
  {:datastore   (jdbc/sql-database {:connection-uri "jdbc:postgresql://localhost:5432/kitella"})
   :migrations (jdbc/load-resources "migrations")})

(defn migrate []
  (repl/migrate config))

(defn rollback []
  (repl/rollback config))