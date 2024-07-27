(import os
        [utils.file_ops [read-file write-file create-directory get-file-metadata copy-file move-file delete-file]]
        [library_study [main :as study-libraries]]
        [filesystem_analyzer [main :as analyze-filesystem]]
        [higher_order_operads [main :as explore-higher-order-operads]])

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

(defn list-files [directory]
  (setv file-list [])
  (for [file (os.listdir directory)]
    (setv filepath (os.path.join directory file))
    (when (os.path.isfile filepath)
      (setv metadata (get-file-metadata filepath))
      (.append file-list (, file metadata))))
  file-list)

(defn display-file-contents [filename]
  (setv content (read-file filename))
  (markdown-section (+ "Contents of " filename)
    (print "```")
    (print content)
    (print "```")))

(defn perform-file-operations []
  (markdown-section "File Operations"
    (print "1. List files\n2. Display file contents\n3. Create a new directory\n4. Write to a file\n5. Copy a file\n6. Move a file\n7. Delete a file\n8. Recursively enumerate directory\n9. Return to main menu")
    
    (setv choice (input "Enter your choice (1-9): "))
    
    (cond
      [(= choice "1") (print (list-files (input "Enter the directory path: ")))]
      [(= choice "2") (display-file-contents (input "Enter the filename to display: "))]
      [(= choice "3") (create-directory (input "Enter the name of the new directory: "))]
      [(= choice "4") (write-file (input "Enter the filename to write to: ") (input "Enter the content to write: "))]
      [(= choice "5") (copy-file (input "Enter the source filename: ") (input "Enter the destination filename: "))]
      [(= choice "6") (move-file (input "Enter the source filename: ") (input "Enter the destination filename: "))]
      [(= choice "7") (delete-file (input "Enter the filename to delete: "))]
      [(= choice "8") (print (recursive-enumerate (input "Enter the directory path to enumerate: ")))]
      [(= choice "9") (return)]
      [True (print "Invalid choice. Please try again.")])))

(defn main []
  (while True
    (markdown-section "Main Menu"
      (print "1. List files and perform file operations\n2. Study library capabilities\n3. Analyze filesystem structure\n4. Explore higher-order operads\n5. Exit")
      (setv choice (input "Enter your choice (1-5): "))

      (cond
        [(= choice "1") (perform-file-operations)]
        [(= choice "2") (study-libraries)]
        [(= choice "3") (analyze-filesystem "filesystem_structure.xml")]
        [(= choice "4") (explore-higher-order-operads)]
        [(= choice "5") (print "Exiting the program. Goodbye!") (break)]
        [True (print "Invalid choice. Please try again.")]))))

(when (= __name__ "__main__")
  (main))
