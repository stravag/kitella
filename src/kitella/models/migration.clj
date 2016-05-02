(ns kitella.models.migration
  (:require [clojure.java.jdbc :as sql]
            [kitella.models.player :as player]))

(defn migrated? []
  (-> (sql/query player/spec
                 [(str "select count(*) from information_schema.tables "
                       "where table_name='players'")])
      first :count pos?))

(defn migrate []
  (when (not (migrated?))
    (print "Creating database structure...") (flush)
    (sql/db-do-commands player/spec
                        (sql/create-table-ddl
                          :players
                          [:id :serial "PRIMARY KEY"]
                          [:body :varchar "NOT NULL"]
                          [:created_at :timestamp
                           "NOT NULL" "DEFAULT CURRENT_TIMESTAMP"]))
    (println " done")))
