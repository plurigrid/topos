import os
import shutil
from datetime import datetime

def get_file_metadata(filepath):
    """Get metadata for a file."""
    try:
        stat = os.stat(filepath)
        return {
            'size': stat.st_size,
            'created': datetime.fromtimestamp(stat.st_ctime).strftime('%Y-%m-%d %H:%M:%S'),
            'modified': datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
        }
    except OSError as e:
        return f"Error getting file metadata: {str(e)}"

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

def copy_file(src, dst):
    """Copy a file from src to dst."""
    try:
        shutil.copy2(src, dst)
        return f"Successfully copied {src} to {dst}"
    except IOError as e:
        return f"Error copying file: {str(e)}"

def move_file(src, dst):
    """Move a file from src to dst."""
    try:
        shutil.move(src, dst)
        return f"Successfully moved {src} to {dst}"
    except IOError as e:
        return f"Error moving file: {str(e)}"

def delete_file(filename):
    """Delete a file."""
    try:
        os.remove(filename)
        return f"Successfully deleted {filename}"
    except IOError as e:
        return f"Error deleting file: {str(e)}"
