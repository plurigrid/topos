(ns main
  (:require [clojure.string :as str]
            [babashka.process :refer [shell]]))

(defn process-input [input]
  (if (str/starts-with? input "hy:")
    (let [hy-code (subs input 3)
          result (shell {:out :string} "hy" "-c" hy-code)]
      (str "Hy result: " (:out result)))
    (str "Babashka result: " input)))

(defn main-loop []
  (println "Welcome to the Babashka-Hy REPL!")
  (println "Type 'exit' to quit.")
  (println "Prefix Hy code with 'hy:' to execute it in Hy.")
  (loop []
    (print "bb-hy> ")
    (flush)
    (let [input (str/trim (read-line))]
      (if (= input "exit")
        (println "Goodbye!")
        (do
          (println (process-input input))
          (recur))))))

(main-loop)
