import random
import subprocess
import importlib
import os
import sys
import json
import hashlib
import datetime
from typing import List, Dict, Any

def self_verify() -> Dict[str, Any]:
    """Perform self-verification of the project."""
    print("Performing self-verification...")
    results = {}
    
    # Check if all required modules can be imported
    required_modules = [
        "discopy", "catgrad", "lambeq", "duckdb", "hy", "ripser", "networkx",
        "torch", "openai", "polars", "matplotlib", "numpy", "nats"
    ]
    results["modules"] = {}
    for module in required_modules:
        try:
            importlib.import_module(module)
            results["modules"][module] = True
            print(f"✓ {module} imported successfully")
        except ImportError:
            results["modules"][module] = False
            print(f"✗ Failed to import {module}")
    
    # Check if key files exist
    key_files = [
        "src/markdown_embedder.py",
        "src/filesystem_analyzer.py",
        "src/higher_order_operads.py",
        "Justfile"
    ]
    results["files"] = {}
    for file in key_files:
        if os.path.exists(file):
            results["files"][file] = True
            print(f"✓ {file} exists")
        else:
            results["files"][file] = False
            print(f"✗ {file} not found")
    
    # Run tests
    test_result = subprocess.run(["pytest"], capture_output=True, text=True)
    results["tests"] = test_result.returncode == 0
    if results["tests"]:
        print("✓ All tests passed")
    else:
        print("✗ Some tests failed")
        print(test_result.stdout)
    
    # Check project hash
    results["project_hash"] = calculate_project_hash()
    print(f"Project hash: {results['project_hash']}")
    
    return results

def meta_self_verify() -> Dict[str, Any]:
    """Perform meta-self-verification of the project."""
    print("Performing meta-self-verification...")
    results = {}
    
    # Check code quality
    quality_checks = [
        ("black", ["black", "--check", "."]),
        ("mypy", ["mypy", "."]),
        ("pylint", ["pylint", "src"])
    ]
    
    results["code_quality"] = {}
    for check_name, command in quality_checks:
        result = subprocess.run(command, capture_output=True, text=True)
        results["code_quality"][check_name] = result.returncode == 0
        if results["code_quality"][check_name]:
            print(f"✓ {check_name} check passed")
        else:
            print(f"✗ {check_name} check failed")
            print(result.stdout)
    
    # Check if the project structure is consistent
    expected_dirs = ["src", "tests", "experiments"]
    results["project_structure"] = {}
    for dir_name in expected_dirs:
        results["project_structure"][dir_name] = os.path.isdir(dir_name)
        if results["project_structure"][dir_name]:
            print(f"✓ {dir_name} directory exists")
        else:
            print(f"✗ {dir_name} directory not found")
    
    # Check for circular dependencies
    results["circular_dependencies"] = check_circular_dependencies()
    if results["circular_dependencies"]:
        print("✗ Circular dependencies detected")
    else:
        print("✓ No circular dependencies detected")
    
    return results

def random_action() -> str:
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
    return action

def launch_loop():
    """Launch into the loop using Justfile random walk over random actions."""
    loop_count = 0
    max_loops = 100  # Prevent infinite loops
    while loop_count < max_loops:
        self_verify_results = self_verify()
        meta_self_verify_results = meta_self_verify()
        
        if all(self_verify_results.values()) and all(meta_self_verify_results.values()):
            action = random_action()
            log_action(action, self_verify_results, meta_self_verify_results)
        else:
            print("Self-verification failed. Exiting loop.")
            break
        
        loop_count += 1
    
    if loop_count == max_loops:
        print(f"Reached maximum number of loops ({max_loops}). Exiting.")

def calculate_project_hash() -> str:
    """Calculate a hash of the entire project."""
    hasher = hashlib.sha256()
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith((".py", ".md", ".txt", ".json")):
                file_path = os.path.join(root, file)
                with open(file_path, "rb") as f:
                    hasher.update(f.read())
    return hasher.hexdigest()

def check_circular_dependencies() -> List[str]:
    """Check for circular dependencies in the project."""
    # This is a simplified check and may need to be expanded for more complex projects
    import networkx as nx
    
    G = nx.DiGraph()
    for root, _, files in os.walk("src"):
        for file in files:
            if file.endswith(".py"):
                module_name = os.path.splitext(file)[0]
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    content = f.read()
                    for line in content.split("\n"):
                        if line.startswith("from") or line.startswith("import"):
                            imported_module = line.split()[1].split(".")[0]
                            G.add_edge(module_name, imported_module)
    
    try:
        cycle = nx.find_cycle(G)
        return [node for node, _ in cycle]
    except nx.NetworkXNoCycle:
        return []

def log_action(action: str, self_verify_results: Dict[str, Any], meta_self_verify_results: Dict[str, Any]):
    """Log the action and verification results."""
    log_entry = {
        "action": action,
        "self_verify_results": self_verify_results,
        "meta_self_verify_results": meta_self_verify_results,
        "timestamp": datetime.datetime.now().isoformat()
    }
    with open("action_log.json", "a") as f:
        json.dump(log_entry, f)
        f.write("\n")

if __name__ == "__main__":
    launch_loop()
