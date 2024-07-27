import os

def list_files():
    """List all files in the current directory."""
    return [f for f in os.listdir('.') if os.path.isfile(f)]

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
        display_file_contents(file)

if __name__ == "__main__":
    main()
