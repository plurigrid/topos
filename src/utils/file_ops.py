import os

def read_file(filename):
    """Read and return the contents of a file."""
    try:
        with open(filename, 'r') as file:
            return file.read()
    except IOError as e:
        return f"Error reading file: {str(e)}"

def write_file(filename, content):
    """Write content to a file."""
    try:
        with open(filename, 'w') as file:
            file.write(content)
        return f"Successfully wrote to {filename}"
    except IOError as e:
        return f"Error writing to file: {str(e)}"

def create_directory(directory):
    """Create a new directory."""
    try:
        os.makedirs(directory, exist_ok=True)
        return f"Successfully created directory: {directory}"
    except OSError as e:
        return f"Error creating directory: {str(e)}"
