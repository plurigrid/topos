(import os)
(import [utils.file_ops [read-file write-file create-directory get-file-metadata copy-file move-file delete-file]])
(import [library_study [main :as study-libraries]])
(import [filesystem_analyzer [main :as analyze-filesystem]])
(import [higher_order_operads [main :as higher-order-operads]])

(defmacro temporal-action [name precondition action postcondition]
  `(defn ~name []
     (when ~precondition
       ~action
       (assert ~postcondition))))

(defmacro markdown-section [title &rest content]
  `(do
     (print (+ "# " ~title))
     ~@content
     (print)))

(temporal-action list-files
  (os.path.exists directory)
  (do
    (setv file-list [])
    (for [file (os.listdir directory)]
      (setv filepath (os.path.join directory file))
      (when (os.path.isfile filepath)
        (setv metadata (get-file-metadata filepath))
        (.append file-list (, file metadata))))
    file-list)
  (isinstance file-list list))

(temporal-action display-file-contents
  (os.path.isfile filename)
  (do
    (setv content (read-file filename))
    (markdown-section (+ "Contents of " filename)
      (print "```")
      (print content)
      (print "```")))
  True)

(defn perform-file-operations []
  (markdown-section "File Operations"
    (print "1. List files")
    (print "2. Display file contents")
    (print "3. Create a new directory")
    (print "4. Write to a file")
    (print "5. Copy a file")
    (print "6. Move a file")
    (print "7. Delete a file")
    (print "8. Return to main menu")
    
    (setv choice (input "Enter your choice (1-8): "))
    
    (cond
      [(= choice "1")
       (list-files)]
      [(= choice "2")
       (setv filename (input "Enter the filename to display: "))
       (display-file-contents filename)]
      [(= choice "3")
       (setv new-dir (input "Enter the name of the new directory: "))
       (create-directory new-dir)]
      [(= choice "4")
       (setv filename (input "Enter the filename to write to: "))
       (setv content (input "Enter the content to write: "))
       (write-file filename content)]
      [(= choice "5")
       (setv src (input "Enter the source filename: "))
       (setv dst (input "Enter the destination filename: "))
       (copy-file src dst)]
      [(= choice "6")
       (setv src (input "Enter the source filename: "))
       (setv dst (input "Enter the destination filename: "))
       (move-file src dst)]
      [(= choice "7")
       (setv filename (input "Enter the filename to delete: "))
       (delete-file filename)]
      [(= choice "8")
       (return)]
      [True
       (print "Invalid choice. Please try again.")])))

(defn main []
  (while True
    (markdown-section "Main Menu"
      (print "1. List files and perform file operations")
      (print "2. Study library capabilities")
      (print "3. Analyze filesystem structure")
      (print "4. Explore higher-order operads")
      (print "5. Exit")
      (setv choice (input "Enter your choice (1-5): "))

      (cond
        [(= choice "1")
         (perform-file-operations)]
        [(= choice "2")
         (study-libraries)]
        [(= choice "3")
         (analyze-filesystem "filesystem_structure.xml")]
        [(= choice "4")
         (higher-order-operads)]
        [(= choice "5")
         (print "Exiting the program. Goodbye!")
         (break)]
        [True
         (print "Invalid choice. Please try again.")]))))

(when (= __name__ "__main__")
  (main))
