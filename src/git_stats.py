import subprocess
from typing import Dict, Any, List, Tuple
from datetime import datetime, timedelta
import time
import random
from collections import Counter

def check_large_commits(days: int = 30, threshold: int = 1000) -> List[Tuple[str, int, str]]:
    """Check for unusually large commits in the recent history."""
    since_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    result = subprocess.run(["git", "log", f"--since={since_date}", "--pretty=format:%H %ad %s", "--numstat"], capture_output=True, text=True)
    lines = result.stdout.split('\n')
    
    large_commits = []
    current_commit = None
    current_changes = 0
    
    for line in lines:
        if line.strip() == '':
            if current_commit and current_changes > threshold:
                large_commits.append((current_commit[0], current_changes, current_commit[1]))
            current_commit = None
            current_changes = 0
        elif current_commit is None:
            current_commit = line.split(' ', 1)
        else:
            try:
                added, removed, _ = line.split('\t')
                current_changes += int(added) + int(removed)
            except ValueError:
                pass
    
    return large_commits

def create_ascii_art() -> str:
    """Create ASCII art representation of recent intent based on git commit history."""
    ascii_art = """
    Recent Intent:
      _________
     /         \\
    |  Ripser   |
    | & Lambeq  |
    |Integration|
    |    +      |
    | Markdown  |
    | Embedding |
     \\_________/
    """
    return ascii_art

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

def count_recent_commits(days: int = 30) -> int:
    """Count the number of commits in the last specified number of days."""
    since_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    result = subprocess.run(["git", "rev-list", "--count", f"--since={since_date}", "HEAD"], capture_output=True, text=True)
    return int(result.stdout.strip())

def estimate_commits_over_time(days: int = 365, interval: int = 30) -> List[Tuple[str, int]]:
    """Estimate commits over time for the past year, grouped by month."""
    commits_over_time = []
    for i in range(0, days, interval):
        end_date = (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d")
        start_date = (datetime.now() - timedelta(days=i+interval)).strftime("%Y-%m-%d")
        result = subprocess.run(["git", "rev-list", "--count", f"--since={start_date}", f"--until={end_date}", "HEAD"], capture_output=True, text=True)
        commits_over_time.append((start_date, int(result.stdout.strip())))
    return list(reversed(commits_over_time))

def visualize_commits_over_time(commits_over_time: List[Tuple[str, int]]):
    """Visualize commits over time using ASCII art."""
    max_commits = max(count for _, count in commits_over_time)
    scale = 20 / max_commits if max_commits > 0 else 1
    
    print("\nCommits over time (ASCII chart):")
    for date, count in commits_over_time:
        bar = '█' * int(count * scale)
        print(f"{date}: {bar} ({count})")

def estimate_features_over_time(days: int = 365, interval: int = 30) -> List[Tuple[str, int]]:
    """Estimate features/capabilities over time based on file changes."""
    features_over_time = []
    for i in range(0, days, interval):
        end_date = (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d")
        start_date = (datetime.now() - timedelta(days=i+interval)).strftime("%Y-%m-%d")
        result = subprocess.run(["git", "diff", "--name-only", f"--since={start_date}", f"--until={end_date}"], capture_output=True, text=True)
        unique_files = len(set(result.stdout.strip().split("\n")))
        features_over_time.append((start_date, unique_files))
    return list(reversed(features_over_time))

def get_most_active_files(limit: int = 10) -> List[Tuple[str, int]]:
    """Get the most frequently changed files in the repository."""
    result = subprocess.run(["git", "log", "--pretty=format:", "--name-only"], capture_output=True, text=True)
    files = result.stdout.strip().split("\n")
    file_counts = Counter(files)
    return file_counts.most_common(limit)

def create_commit_evolution_cartoon(iterations: int = 69):
    creatures = ['🐟', '🐸', '🦎', '🐒', '🦍', '🧑‍💻']
    environment = ['🌊', '🏝️', '🌴', '🌳', '🏙️', '💻']
    
    for i in range(iterations):
        creature = creatures[min(i // 12, len(creatures) - 1)]
        env = environment[min(i // 12, len(environment) - 1)]
        
        print(f"\rIteration {i+1}: {env * 10}")
        print(f"{' ' * (i % 10)}{creature}")
        print(f"{'🧬' * (i + 1)}")
        
        time.sleep(0.1)
        if i < iterations - 1:
            print("\033[3A")  # Move cursor up 3 lines

def print_git_stats():
    stats = get_git_stats()
    print(create_ascii_art())
    print("Git Repository Statistics:")
    print(f"Total commits: {stats['total_commits']}")
    print(f"Number of branches: {stats['branch_count']}")
    print(f"Number of contributors: {stats['contributor_count']}")
    print(f"Total number of files: {stats['file_count']}")
    
    recent_commits = count_recent_commits()
    print(f"\nRecent activity:")
    print(f"Commits in the last 30 days: {recent_commits}")
    
    commits_over_time = estimate_commits_over_time()
    visualize_commits_over_time(commits_over_time)
    
    print("\nFeatures/capabilities over time (last year, monthly):")
    features_over_time = estimate_features_over_time()
    for date, count in features_over_time:
        print(f"{date}: {count} file changes")
    
    print("\nChecking for unusually large commits in the last 30 days:")
    large_commits = check_large_commits()
    if large_commits:
        print("Found potentially problematic large commits:")
        for commit_hash, changes, date in large_commits:
            print(f"Commit {commit_hash[:7]} on {date}: {changes} changes")
    else:
        print("No unusually large commits found in the recent history.")
    
    print("\nMost active files:")
    active_files = get_most_active_files()
    for file, changes in active_files[:10]:
        print(f"{file}: {changes} changes")

    print("\nCommit Evolution Cartoon:")
    create_commit_evolution_cartoon()

if __name__ == "__main__":
    print_git_stats()
