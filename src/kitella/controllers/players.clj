(ns kitella.controllers.players
  (:require [compojure.core :refer [defroutes GET POST]]
            [clojure.string :as str]
            [ring.util.response :as ring]
            [kitella.views.players :as view]
            [kitella.models.player :as model]))

(defn index []
  (view/index (model/all)))

(defn create
  [player]
  (when-not (str/blank? player)
    (model/create player))
  (ring/redirect "/"))

(defroutes routes
           (GET "/" [] (index))
           (POST "/" [player] (create player)))