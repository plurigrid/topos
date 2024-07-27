import subprocess
import math
import zlib

def get_git_history():
    """Retrieve the git commit history."""
    return subprocess.check_output(['git', 'log', '--pretty=format:%H']).decode('utf-8').split('\n')

def get_diff(commit1, commit2):
    """Get the diff between two commits."""
    return subprocess.check_output(['git', 'diff', commit1, commit2]).decode('utf-8')

def estimate_kolmogorov_complexity(data):
    """Estimate Kolmogorov complexity using compression."""
    return len(zlib.compress(data.encode('utf-8')))

def calculate_information_saturation_rate(history, window_size=10):
    """Calculate the rate of information saturation."""
    complexities = []
    for i in range(len(history) - window_size):
        window = history[i:i+window_size]
        diffs = [get_diff(window[j], window[j+1]) for j in range(len(window)-1)]
        combined_diff = ''.join(diffs)
        complexity = estimate_kolmogorov_complexity(combined_diff)
        complexities.append(complexity)
    
    # Calculate the rate of change in complexity
    rates = [complexities[i+1] - complexities[i] for i in range(len(complexities)-1)]
    return sum(rates) / len(rates) if rates else 0

def main():
    history = get_git_history()
    rate = calculate_information_saturation_rate(history)
    print(f"Rate of information saturation: {rate}")
    print(f"Estimated Kolmogorov complexity of latest commit: {estimate_kolmogorov_complexity(get_diff(history[1], history[0]))}")

if __name__ == "__main__":
    main()
