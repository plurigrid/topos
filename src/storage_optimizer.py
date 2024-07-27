import os
import shutil
from collections import defaultdict

def analyze_storage():
    """Analyze current storage usage."""
    total, used, free = shutil.disk_usage("/")
    print(f"Total: {total // (2**30)} GB")
    print(f"Used: {used // (2**30)} GB")
    print(f"Free: {free // (2**30)} GB")
    print(f"Usage: {used / total:.2%}")

def find_duplicate_files(directory):
    """Find duplicate files based on size and first 1024 bytes."""
    file_dict = defaultdict(list)
    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            try:
                file_size = os.path.getsize(filepath)
                with open(filepath, 'rb') as f:
                    file_hash = hash(f.read(1024))
                file_dict[(file_size, file_hash)].append(filepath)
            except (IOError, OSError):
                continue
    return {k: v for k, v in file_dict.items() if len(v) > 1}

def compress_files(directory, extensions):
    """Compress files with specified extensions."""
    import gzip
    for root, _, files in os.walk(directory):
        for filename in files:
            if any(filename.endswith(ext) for ext in extensions):
                filepath = os.path.join(root, filename)
                with open(filepath, 'rb') as f_in:
                    with gzip.open(f"{filepath}.gz", 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)
                os.remove(filepath)
                print(f"Compressed: {filepath}")

def optimize_storage(directory):
    """Run storage optimization techniques."""
    print("Analyzing storage...")
    analyze_storage()
    
    print("\nFinding duplicate files...")
    duplicates = find_duplicate_files(directory)
    for files in duplicates.values():
        print(f"Duplicate files: {', '.join(files)}")
    
    print("\nCompressing large text files...")
    compress_files(directory, ['.txt', '.log', '.md'])
    
    print("\nStorage optimization complete.")

if __name__ == "__main__":
    optimize_storage('.')
