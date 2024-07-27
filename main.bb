(ns main
  (:require [clojure.string :as str]))

(defn process-input [input]
  (str "You entered: " input))

(defn main-loop []
  (println "Welcome to the Babashka REPL!")
  (println "Type 'exit' to quit.")
  (loop []
    (print "bb> ")
    (flush)
    (let [input (str/trim (read-line))]
      (if (= input "exit")
        (println "Goodbye!")
        (do
          (println (process-input input))
          (recur))))))

(main-loop)
