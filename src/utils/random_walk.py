import os
import random
import concurrent.futures
import threading

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

def random_walk(start_dir='.', max_depth=3, max_files=5, structure=None):
    """
    Perform a random walk through the project structure.
    
    :param start_dir: The directory to start the walk from
    :param max_depth: Maximum depth to explore
    :param max_files: Maximum number of files to examine at each level
    :param structure: DirectoryStructure object to update
    """
    global active_walks
    with active_walks_lock:
        active_walks += 1
        print(f"Active random walks: {active_walks}")

    try:
        for root, dirs, files in os.walk(start_dir):
            if root.count(os.sep) - start_dir.count(os.sep) >= max_depth:
                del dirs[:]
            else:
                if structure:
                    structure.add_directory(root)
                print(f"\nExploring directory: {root}")
                sampled_files = random.sample(files, min(max_files, len(files)))
                for file in sampled_files:
                    file_path = os.path.join(root, file)
                    if structure:
                        structure.add_file(file_path)
                    print(f"  - {file}")
                    try:
                        with open(file_path, 'r') as f:
                            first_line = next(f, '').strip()
                            print(f"    First line: {first_line[:50]}...")
                    except Exception as e:
                        print(f"    Error reading file: {str(e)}")
    finally:
        with active_walks_lock:
            active_walks -= 1
            print(f"Active random walks: {active_walks}")

def concurrent_random_walks(num_walks=3, start_dir='.', max_depth=3, max_files=5):
    structure = DirectoryStructure()
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_walks) as executor:
        futures = [executor.submit(random_walk, start_dir, max_depth, max_files, structure) for _ in range(num_walks)]
        concurrent.futures.wait(futures)
    return structure

if __name__ == "__main__":
    result_structure = concurrent_random_walks()
    print("\nFinal Directory Structure:")
    print(result_structure.structure)
