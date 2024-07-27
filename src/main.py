import os
from utils.file_ops import read_file, write_file, create_directory, get_file_metadata
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
    print(read_file(filename))
    print("\n" + "-"*50 + "\n")

def main():
    print("Choose an option:")
    print("1. List files and perform file operations")
    print("2. Study library capabilities")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        perform_file_operations()
    elif choice == '2':
        study_libraries()
    else:
        print("Invalid choice. Exiting.")

def perform_file_operations():
    print("1. Listing files with metadata in the current directory:")
    files = list_files()
    for file, metadata in files:
        print(f"File: {file}")
        print(f"  Size: {metadata['size']} bytes")
        print(f"  Created: {metadata['created']}")
        print(f"  Modified: {metadata['modified']}")
        print()
    
    print("\n2. Displaying contents of each file:")
    for file, _ in files:
        try:
            display_file_contents(file)
        except Exception as e:
            print(f"Error reading {file}: {str(e)}")
            print("\n" + "-"*50 + "\n")
    
    print("3. Creating a new directory:")
    new_dir = "new_directory"
    print(create_directory(new_dir))
    
    print("\n4. Writing to a new file:")
    new_file = os.path.join(new_dir, "new_file.txt")
    content = "This is a new file created by the program."
    print(write_file(new_file, content))
    
    print("\n5. Reading the newly created file:")
    display_file_contents(new_file)
    
    print("\n6. Listing files with metadata including subdirectories:")
    all_files = list_files(include_subdirs=True)
    for file, metadata in all_files:
        print(f"File: {file}")
        print(f"  Size: {metadata['size']} bytes")
        print(f"  Created: {metadata['created']}")
        print(f"  Modified: {metadata['modified']}")
        print()

if __name__ == "__main__":
    main()
