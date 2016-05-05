; TODO fix this!

(ns kitella.persistence.db)
(use 'korma.db)
(use 'korma.core)

;; See: http://sqlkorma.com/docs#db
(defdb prod (postgres {:db         "kitella"
                       :user       ""
                       :password   ""
                       :host       "localhost"
                       :port       "5432"}))

(declare events players classifications)

(defentity events
           (pk :id)
           (table :events)
           (entity-fields :name :description)
           (many-to-many players :events_players))

(defentity players
           (pk :id)
           (table :players)
           (entity-fields :firstname :lastname :email)
           (many-to-many events :events_players))

(defn select-players-by-event [id]
  (select players
          (with events)
          (where {:events.id id})))

(defn select-events
  (select events
          (with players)))