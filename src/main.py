import os

def list_files(include_subdirs=False):
    """
    List all files in the current directory.
    If include_subdirs is True, also list files in subdirectories.
    """
    current_dir = os.getcwd()
    print(f"Current directory: {current_dir}")
    
    if include_subdirs:
        file_list = []
        for root, dirs, files in os.walk(current_dir):
            for file in files:
                file_list.append(os.path.join(root, file))
        return file_list
    else:
        return [f for f in os.listdir(current_dir) if os.path.isfile(os.path.join(current_dir, f))]

def read_file(filename):
    """Read and return the contents of a file."""
    try:
        with open(filename, 'r') as file:
            return file.read()
    except IOError as e:
        return f"Error reading file: {str(e)}"

def display_file_contents(filename):
    """Display the contents of a file."""
    print(f"Contents of {filename}:")
    print(read_file(filename))
    print("\n" + "-"*50 + "\n")

def write_file(filename, content):
    """Write content to a file."""
    try:
        with open(filename, 'w') as file:
            file.write(content)
        return f"Successfully wrote to {filename}"
    except IOError as e:
        return f"Error writing to file: {str(e)}"

def main():
    print("Files in the current directory:")
    files = list_files()
    for file in files:
        print(file)
    
    print("\nDisplaying contents of each file:")
    for file in files:
        try:
            display_file_contents(file)
        except Exception as e:
            print(f"Error reading {file}: {str(e)}")
            print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    main()
