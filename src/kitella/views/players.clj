(ns kitella.views.players
  (:require [kitella.views.layout :as layout]
            [hiccup.core :refer [h]]
            [hiccup.form :as form]
            [ring.util.anti-forgery :as anti-forgery]))

(defn player-form []
  [:div {:id "player-form" :class "sixteen columns alpha omega"}
   (form/form-to [:post "/"]
                 (anti-forgery/anti-forgery-field)
                 (form/label "player" "Player name")
                 (form/text-area "player")
                 (form/submit-button "Add player"))])

(defn display-players [players]
  [:div {:class "players sixteen columns alpha omega"}
   (map
     (fn [player] [:h2 {:class "player"} (h (:body player))])
     players)])

(defn index [players]
  (layout/common "Player"
                 (player-form)
                 [:div {:class "clear"}]
                 (display-players players)))