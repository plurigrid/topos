import os
from utils.file_ops import read_file, write_file, create_directory

def list_files(directory=None, include_subdirs=False):
    """
    List all files in the specified directory or current directory if not specified.
    If include_subdirs is True, also list files in subdirectories.
    """
    if directory is None:
        directory = os.getcwd()
    print(f"Listing files in directory: {directory}")
    
    if include_subdirs:
        file_list = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_list.append(os.path.relpath(os.path.join(root, file), directory))
        return file_list
    else:
        return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def display_file_contents(filename):
    """Display the contents of a file."""
    print(f"Contents of {filename}:")
    print(read_file(filename))
    print("\n" + "-"*50 + "\n")

def main():
    print("1. Listing files in the current directory:")
    files = list_files()
    for file in files:
        print(file)
    
    print("\n2. Displaying contents of each file:")
    for file in files:
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

if __name__ == "__main__":
    main()
