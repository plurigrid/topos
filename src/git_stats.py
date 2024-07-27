import subprocess
from typing import Dict, Any

def get_git_stats() -> Dict[str, Any]:
    stats = {}
    
    # Get total number of commits
    result = subprocess.run(["git", "rev-list", "--count", "HEAD"], capture_output=True, text=True)
    stats["total_commits"] = int(result.stdout.strip())
    
    # Get number of branches
    result = subprocess.run(["git", "branch", "--list"], capture_output=True, text=True)
    stats["branch_count"] = len(result.stdout.strip().split("\n"))
    
    # Get number of contributors
    result = subprocess.run(["git", "shortlog", "-sn", "--no-merges"], capture_output=True, text=True)
    stats["contributor_count"] = len(result.stdout.strip().split("\n"))
    
    # Get total number of files
    result = subprocess.run(["git", "ls-files"], capture_output=True, text=True)
    stats["file_count"] = len(result.stdout.strip().split("\n"))
    
    return stats

def print_git_stats():
    stats = get_git_stats()
    print("Git Repository Statistics:")
    print(f"Total commits: {stats['total_commits']}")
    print(f"Number of branches: {stats['branch_count']}")
    print(f"Number of contributors: {stats['contributor_count']}")
    print(f"Total number of files: {stats['file_count']}")

if __name__ == "__main__":
    print_git_stats()
