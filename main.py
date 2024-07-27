import subprocess
from setup_dit import setup_dit
from src.utils.git_diff_detector import (
    get_current_commit_hash,
    establish_diff_detection_rule,
    continuous_git_change_detection,
    run_temporal_lattice_control
)
from src.modal_julia_app import run_modal_julia_app

def run_dit_setup():
    print("Setting up DiT repository...")
    setup_dit()
    print("DiT setup complete.")

def run_julia_exploration():
    print("Running Julia exploration...")
    try:
        result = subprocess.run(["julia", "src/julia_exploration.jl"], capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("Errors encountered:")
            print(result.stderr)
    except FileNotFoundError:
        print("Julia is not installed or not in the system PATH. Please install Julia and try again.")

if __name__ == "__main__":
    session_start_commit = get_current_commit_hash()
    diff_detection_rule = establish_diff_detection_rule(session_start_commit)
    continuous_git_change_detection()

    run_dit_setup()

    if diff_detection_rule():
        print("Unexpected changes detected. Please review and handle accordingly.")

    print("\nRunning Temporal Lattice Control Simulation:")
    run_temporal_lattice_control()

    print("\nWould you like to run the Julia exploration? (y/n)")
    choice = input().lower()
    if choice == 'y':
        run_julia_exploration()

    print("\nWould you like to run the Modal Julia app? (y/n)")
    choice = input().lower()
    if choice == 'y':
        run_modal_julia_app()
