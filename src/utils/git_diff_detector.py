import subprocess
import os

def get_current_commit_hash():
    """Get the current commit hash."""
    return subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('ascii').strip()

def get_diff_since_commit(commit_hash):
    """Get the diff since the given commit hash."""
    return subprocess.check_output(['git', 'diff', commit_hash]).decode('ascii')

def detect_unexpected_diffs(session_start_commit):
    """Detect unexpected diffs since the start of the session."""
    current_commit = get_current_commit_hash()
    if current_commit != session_start_commit:
        diff = get_diff_since_commit(session_start_commit)
        if diff:
            print("Warning: Unexpected changes detected since the start of the session.")
            print("Diff:")
            print(diff)
            return True
    return False

def establish_diff_detection_rule(session_start_commit):
    """Establish a rule for detecting unexpected diffs."""
    def check_for_unexpected_diffs():
        return detect_unexpected_diffs(session_start_commit)
    return check_for_unexpected_diffs

# Usage example:
# session_start_commit = get_current_commit_hash()
# diff_detection_rule = establish_diff_detection_rule(session_start_commit)
# 
# # Later in the session:
# if diff_detection_rule():
#     print("Unexpected changes detected. Please review and handle accordingly.")
