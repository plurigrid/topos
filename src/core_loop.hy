(import os)
(import [utils.file_ops [read-file write-file create-directory get-file-metadata copy-file move-file delete-file]])
(import [library_study [main :as study-libraries]])

(defn list-files [&optional [directory None] [include-subdirs False]]
  "List all files with metadata in the specified directory or current directory if not specified.
   If include-subdirs is True, also list files in subdirectories."
  (setv directory (if (is directory None) (os.getcwd) directory))
  (print f"Listing files in directory: {directory}")
  
  (setv file-list [])
  (if include-subdirs
      (for [(, root dirs files) (os.walk directory)]
        (for [file files]
          (setv filepath (os.path.join root file))
          (setv relative-path (os.path.relpath filepath directory))
          (setv metadata (get-file-metadata filepath))
          (.append file-list (, relative-path metadata))))
      (for [file (os.listdir directory)]
        (setv filepath (os.path.join directory file))
        (when (os.path.isfile filepath)
          (setv metadata (get-file-metadata filepath))
          (.append file-list (, file metadata)))))
  
  file-list)

(defn display-file-contents [filename]
  "Display the contents of a file."
  (print f"Contents of {filename}:")
  (setv content (read-file filename))
  (if (isinstance content str)
      (print content)
      (print "Unable to display file contents."))
  (print "\n" (* "-" 50) "\n"))

(defn perform-file-operations []
  (while True
    (print "\nFile Operations:")
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
       (setv include-subdirs (= (.lower (input "Include subdirectories? (y/n): ")) "y"))
       (setv files (list-files :include-subdirs include-subdirs))
       (for [(, file metadata) files]
         (print f"File: {file}")
         (print f"  Size: {(get metadata 'size')} bytes")
         (print f"  Created: {(get metadata 'created')}")
         (print f"  Modified: {(get metadata 'modified')}")
         (print))]
      [(= choice "2")
       (setv filename (input "Enter the filename to display: "))
       (display-file-contents filename)]
      [(= choice "3")
       (setv new-dir (input "Enter the name of the new directory: "))
       (print (create-directory new-dir))]
      [(= choice "4")
       (setv filename (input "Enter the filename to write to: "))
       (setv content (input "Enter the content to write: "))
       (print (write-file filename content))]
      [(= choice "5")
       (setv src (input "Enter the source filename: "))
       (setv dst (input "Enter the destination filename: "))
       (print (copy-file src dst))]
      [(= choice "6")
       (setv src (input "Enter the source filename: "))
       (setv dst (input "Enter the destination filename: "))
       (print (move-file src dst))]
      [(= choice "7")
       (setv filename (input "Enter the filename to delete: "))
       (print (delete-file filename))]
      [(= choice "8")
       (break)]
      [True
       (print "Invalid choice. Please try again.")])))

(defn main []
  (while True
    (print "\nChoose an option:")
    (print "1. List files and perform file operations")
    (print "2. Study library capabilities")
    (print "3. Exit")
    (setv choice (input "Enter your choice (1, 2, or 3): "))

    (cond
      [(= choice "1")
       (perform-file-operations)]
      [(= choice "2")
       (study-libraries)]
      [(= choice "3")
       (print "Exiting the program. Goodbye!")
       (break)]
      [True
       (print "Invalid choice. Please try again.")])))

(when (= __name__ "__main__")
  (main))
