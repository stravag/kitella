(defproject kitella "0.0.1-SNAPSHOT"
  :description "Disabled Sports Classification Application"
  :url "https://github.com/stravag/kitella"
  :min-lein-version "2.0.0"
  :license {:name "Eclipse Public License"
            :url  "http://www.eclipse.org/legal/epl-v10.html"}
  :dependencies [[org.clojure/clojure "1.8.0"]
                 [org.clojure/java.jdbc "0.5.8"]
                 [org.postgresql/postgresql "9.4.1208.jre7"]
                 [ragtime "0.5.2"]
                 [ring/ring-jetty-adapter "1.4.0"]
                 [compojure "1.5.0"]
                 [ring/ring-defaults "0.2.0"]
                 [hiccup "1.0.5"]]
  :main ^:skip-aot kitella.web
  :uberjar-name "kitella-standalone.jar"
  :plugins [[lein-ring "0.8.13"]]
  :ring {:handler kitella.web/application
         :init    kitella.models.migration/migrate}
  :profiles {:dev     {:dependencies [[javax.servlet/servlet-api "2.5"]
                                      [ring-mock "0.1.5"]]}
             :uberjar {:aot :all}}
  :aliases {"migrate"  ["run" "-m" "kitella.models.migration/migrate"]
            "rollback" ["run" "-m" "kitella.models.migration/rollback"]})
