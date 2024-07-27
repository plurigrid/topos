import os
import random
import concurrent.futures
import threading
import time

class DirectoryStructure:
    def __init__(self):
        self.structure = {}
        self.lock = threading.Lock()

    def add_directory(self, path):
        with self.lock:
            current = self.structure
            for part in path.split(os.sep):
                if part not in current:
                    current[part] = {}
                current = current[part]

    def add_file(self, path):
        dir_path, filename = os.path.split(path)
        self.add_directory(dir_path)
        with self.lock:
            current = self.structure
            for part in dir_path.split(os.sep):
                current = current[part]
            if 'files' not in current:
                current['files'] = []
            current['files'].append(filename)

active_walks = 0
active_walks_lock = threading.Lock()

def random_walk(target_file=None, max_lines=5):
    """
    Perform a random walk through the project structure or a specific file.
    
    :param target_file: The specific file to walk through (e.g., 'Justfile')
    :param max_lines: Maximum number of lines to examine
    """
    global active_walks
    with active_walks_lock:
        active_walks += 1
        print(f"Active random walks: {active_walks}")

    try:
        if target_file and os.path.isfile(target_file):
            print(f"\nExploring file: {target_file}")
            with open(target_file, 'r') as f:
                lines = f.readlines()
                sampled_lines = random.sample(lines, min(max_lines, len(lines)))
                for i, line in enumerate(sampled_lines, 1):
                    print(f"  Line {i}: {line.strip()}")
            print(f"File size: {os.path.getsize(target_file)} bytes")
            print(f"Last modified: {time.ctime(os.path.getmtime(target_file))}")
        else:
            for root, dirs, files in os.walk('.'):
                print(f"\nExploring directory: {root}")
                print(f"Number of subdirectories: {len(dirs)}")
                print(f"Number of files: {len(files)}")
                sampled_files = random.sample(files, min(5, len(files)))
                for file in sampled_files:
                    file_path = os.path.join(root, file)
                    print(f"  - {file}")
                    try:
                        with open(file_path, 'r') as f:
                            first_line = next(f, '').strip()
                            print(f"    First line: {first_line[:50]}...")
                        print(f"    File size: {os.path.getsize(file_path)} bytes")
                        print(f"    Last modified: {time.ctime(os.path.getmtime(file_path))}")
                    except Exception as e:
                        print(f"    Error reading file: {str(e)}")
    finally:
        with active_walks_lock:
            active_walks -= 1
            print(f"Active random walks: {active_walks}")

import random
import subprocess

def concurrent_random_walks(num_walks=3, target_file=None, max_lines=5):
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_walks) as executor:
        futures = [executor.submit(random_walk, target_file, max_lines) for _ in range(num_walks)]
        concurrent.futures.wait(futures)

if __name__ == "__main__":
    concurrent_random_walks()
def random_walk_justfile():
    """Perform a random walk through the Justfile."""
    try:
        # Get all available tasks from Justfile
        result = subprocess.run(["just", "--list"], capture_output=True, text=True)
        tasks = [line.split()[0] for line in result.stdout.split('\n') if line and not line.startswith(' ')]
        
        # Choose a random task
        task = random.choice(tasks)
        
        print(f"Executing random task: {task}")
        
        # Execute the chosen task
        subprocess.run(["just", task])
        
        return task
    except Exception as e:
        print(f"Error during random walk: {e}")
        return None
