import os
import shutil
from utils.file_ops import read_file, write_file, create_directory, get_file_metadata, copy_file, move_file, delete_file
from library_study import main as study_libraries

def list_files(directory=None, include_subdirs=False):
    """
    List all files with metadata in the specified directory or current directory if not specified.
    If include_subdirs is True, also list files in subdirectories.
    """
    if directory is None:
        directory = os.getcwd()
    print(f"Listing files in directory: {directory}")
    
    file_list = []
    if include_subdirs:
        for root, dirs, files in os.walk(directory):
            for file in files:
                filepath = os.path.join(root, file)
                relative_path = os.path.relpath(filepath, directory)
                metadata = get_file_metadata(filepath)
                file_list.append((relative_path, metadata))
    else:
        for file in os.listdir(directory):
            filepath = os.path.join(directory, file)
            if os.path.isfile(filepath):
                metadata = get_file_metadata(filepath)
                file_list.append((file, metadata))
    
    return file_list

def display_file_contents(filename):
    """Display the contents of a file."""
    print(f"Contents of {filename}:")
    content = read_file(filename)
    if isinstance(content, str):
        print(content)
    else:
        print("Unable to display file contents.")
    print("\n" + "-"*50 + "\n")

def main():
    while True:
        print("\nChoose an option:")
        print("1. List files and perform file operations")
        print("2. Study library capabilities")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            perform_file_operations()
        elif choice == '2':
            study_libraries()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def perform_file_operations():
    while True:
        print("\nFile Operations:")
        print("1. List files")
        print("2. Display file contents")
        print("3. Create a new directory")
        print("4. Write to a file")
        print("5. Copy a file")
        print("6. Move a file")
        print("7. Delete a file")
        print("8. Return to main menu")
        
        choice = input("Enter your choice (1-8): ")
        
        if choice == '1':
            include_subdirs = input("Include subdirectories? (y/n): ").lower() == 'y'
            files = list_files(include_subdirs=include_subdirs)
            for file, metadata in files:
                print(f"File: {file}")
                print(f"  Size: {metadata['size']} bytes")
                print(f"  Created: {metadata['created']}")
                print(f"  Modified: {metadata['modified']}")
                print()
        elif choice == '2':
            filename = input("Enter the filename to display: ")
            display_file_contents(filename)
        elif choice == '3':
            new_dir = input("Enter the name of the new directory: ")
            print(create_directory(new_dir))
        elif choice == '4':
            filename = input("Enter the filename to write to: ")
            content = input("Enter the content to write: ")
            print(write_file(filename, content))
        elif choice == '5':
            src = input("Enter the source filename: ")
            dst = input("Enter the destination filename: ")
            print(copy_file(src, dst))
        elif choice == '6':
            src = input("Enter the source filename: ")
            dst = input("Enter the destination filename: ")
            print(move_file(src, dst))
        elif choice == '7':
            filename = input("Enter the filename to delete: ")
            print(delete_file(filename))
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
