import os

def list_files():
    """List all files in the current directory."""
    current_dir = os.getcwd()
    print(f"Current directory: {current_dir}")
    return [f for f in os.listdir(current_dir) if os.path.isfile(os.path.join(current_dir, f))]

def read_file(filename):
    """Read and return the contents of a file."""
    with open(filename, 'r') as file:
        return file.read()

def display_file_contents(filename):
    """Display the contents of a file."""
    print(f"Contents of {filename}:")
    print(read_file(filename))
    print("\n" + "-"*50 + "\n")

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
