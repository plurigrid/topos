import os
import random

def random_walk(start_dir='.', max_depth=3, max_files=5):
    """
    Perform a random walk through the project structure.
    
    :param start_dir: The directory to start the walk from
    :param max_depth: Maximum depth to explore
    :param max_files: Maximum number of files to examine at each level
    """
    for root, dirs, files in os.walk(start_dir):
        if root.count(os.sep) - start_dir.count(os.sep) >= max_depth:
            del dirs[:]
        else:
            print(f"\nExploring directory: {root}")
            sampled_files = random.sample(files, min(max_files, len(files)))
            for file in sampled_files:
                file_path = os.path.join(root, file)
                print(f"  - {file}")
                try:
                    with open(file_path, 'r') as f:
                        first_line = next(f, '').strip()
                        print(f"    First line: {first_line[:50]}...")
                except Exception as e:
                    print(f"    Error reading file: {str(e)}")

if __name__ == "__main__":
    random_walk()
