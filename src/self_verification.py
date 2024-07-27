import random
import subprocess
import importlib
import os
import sys

def self_verify():
    """Perform self-verification of the project."""
    print("Performing self-verification...")
    
    # Check if all required modules can be imported
    required_modules = [
        "discopy", "catgrad", "lambeq", "duckdb", "hy", "ripser", "networkx",
        "torch", "openai", "polars", "matplotlib", "numpy", "nats"
    ]
    for module in required_modules:
        try:
            importlib.import_module(module)
            print(f"✓ {module} imported successfully")
        except ImportError:
            print(f"✗ Failed to import {module}")
            return False
    
    # Check if key files exist
    key_files = [
        "src/markdown_embedder.py",
        "src/filesystem_analyzer.py",
        "src/higher_order_operads.py",
        "Justfile"
    ]
    for file in key_files:
        if os.path.exists(file):
            print(f"✓ {file} exists")
        else:
            print(f"✗ {file} not found")
            return False
    
    # Run tests
    test_result = subprocess.run(["pytest"], capture_output=True, text=True)
    if test_result.returncode == 0:
        print("✓ All tests passed")
    else:
        print("✗ Some tests failed")
        print(test_result.stdout)
        return False
    
    return True

def meta_self_verify():
    """Perform meta-self-verification of the project."""
    print("Performing meta-self-verification...")
    
    # Check code quality
    quality_checks = [
        ("black", ["black", "--check", "."]),
        ("mypy", ["mypy", "."]),
        ("pylint", ["pylint", "src"])
    ]
    
    for check_name, command in quality_checks:
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✓ {check_name} check passed")
        else:
            print(f"✗ {check_name} check failed")
            print(result.stdout)
            return False
    
    # Check if the project structure is consistent
    expected_dirs = ["src", "tests", "experiments"]
    for dir_name in expected_dirs:
        if os.path.isdir(dir_name):
            print(f"✓ {dir_name} directory exists")
        else:
            print(f"✗ {dir_name} directory not found")
            return False
    
    return True

def random_action():
    """Perform a random action from the Justfile."""
    actions = [
        "study-libraries", "analyze-filesystem", "explore-operads",
        "ripser-lambeq-analysis", "embed-markdown", "analyze-topos",
        "git-stats", "quantum-supermaps", "vsa-deep-learning",
        "acset-schemas", "cognitive-topology", "cobordism-time-travel",
        "tensor-product-modeling", "balanced-ternary-clock",
        "self-aware-geometry", "cybernetic-xenornithology",
        "plurigrid-acquisition"
    ]
    action = random.choice(actions)
    print(f"Performing random action: {action}")
    subprocess.run(["just", action])

def launch_loop():
    """Launch into the loop using Justfile random walk over random actions."""
    while True:
        if self_verify() and meta_self_verify():
            random_action()
        else:
            print("Self-verification failed. Exiting loop.")
            break

if __name__ == "__main__":
    launch_loop()
