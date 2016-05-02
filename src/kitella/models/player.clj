(ns kitella.models.player
  (:require [clojure.java.jdbc :as sql]))

(def spec (or (System/getenv "DATABASE_URL")
              "postgresql://localhost:5432/kitella"))

(defn all []
  (into [] (sql/query spec ["select * from players order by id desc"])))

(defn create [player]
  (sql/insert! spec :players [:body] [player]))
