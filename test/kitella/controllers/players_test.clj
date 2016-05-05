(ns kitella.controllers.players-test
  (:use clojure.test
        ring.mock.request
        kitella.handler))

(deftest test-app
  ;; disabled
  (comment
  (testing "players endpoint"
    (let [response (application (request :get "/players"))]
      (is (= (:status response) 200))
      (is (= (get-in response [:headers "Content-Type"]) "application-json"))))
  )

  (testing "not-found route"
    (let [response (application (request :get "/bogus-route"))]
      (is (= (:status response) 404)))))

