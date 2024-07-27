from setup_dit import setup_dit
from src.utils.git_diff_detector import (
    get_current_commit_hash,
    establish_diff_detection_rule,
    continuous_git_change_detection,
    run_temporal_lattice_control
)

def run_dit_setup():
    print("Setting up DiT repository...")
    setup_dit()
    print("DiT setup complete.")

if __name__ == "__main__":
    session_start_commit = get_current_commit_hash()
    diff_detection_rule = establish_diff_detection_rule(session_start_commit)
    continuous_git_change_detection()

    run_dit_setup()

    if diff_detection_rule():
        print("Unexpected changes detected. Please review and handle accordingly.")

    print("\nRunning Temporal Lattice Control Simulation:")
    run_temporal_lattice_control()
