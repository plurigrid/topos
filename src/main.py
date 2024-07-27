import sys
import unittest
import asyncio
import hy
from hy.cmdline import HyREPL
from src.core_loop import main as hy_main
import exa_py
from src.invariants import print_invariants
from src.quantum_supermaps import run_tests as run_quantum_tests
from src.file_enumerator import enumerate_files
from src.actegories import Actegory, actegory_functor
from src.openai_api_handler import explore_action_space
from src.ripser_lambeq_integration import main as run_ripser_lambeq
from src.markdown_embedder import main as embed_markdown
from src.topos_graph_analyzer import main as analyze_topos
from src.git_stats import print_git_stats
from src.utils.random_walk import concurrent_random_walks
from src.utils.package_discovery import discover_package_methods
from src.storage_optimizer import optimize_storage
from src.nats_knowledge_mutator import NATSKnowledgeMutator
from src.git_complexity_analyzer import main as analyze_git_complexity
from src.screenshot_analyzer import analyze_screenshots_in_directory, eventually_consistent_loop
import subprocess

def run_acsets_analysis():
    print("\nRunning ACSets.jl analysis...")
    try:
        result = subprocess.run(["julia", "src/acsets_integration.jl"], capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("Errors encountered:")
            print(result.stderr)
    except FileNotFoundError:
        print("Julia is not installed or not in the system PATH. Please install Julia and try again.")

def summarize_project_concepts():
    """
    Summarize key concepts and invariants of the project.
    """
    print("\nProject Key Concepts and Invariants:")
    print("1. Persistent Homology: Analyzing topological features across multiple scales")
    print("2. System Dynamics Homology: Studying structural similarities in complex systems")
    print("3. Markov Equivalence Classes: Groups of causal models with the same conditional independence relations")
    print("4. Actegories: Categorical structures combining actions and morphisms")
    print("5. Quantum Supermaps: Higher-order quantum operations")
    print("6. Topos Theory: Categorical approach to the foundations of mathematics")
    print("7. Ripser-Lambeq Integration: Combining topological data analysis with quantum natural language processing")
    print("8. NATS Knowledge Mutation: Distributed system for evolving knowledge structures")
    print("9. Git Complexity Analysis: Assessing project complexity through version control data")
    print("10. Screenshot Analysis: Applying computer vision to analyze desktop screenshots")

def print_chapter_header():
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║                 OPERATIONAL SEMANTICS PROJECT                ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝

    We Try and Try and Try Again Compass:

           N
           |
           |
    W------+------E  "We try and try and try again,
           |         In every direction we extend,
           |         Learning, growing, never pretend,
           S         Our journey of knowledge has no end."

    Cognitive Continuation Diagram:

    ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
    │ Analyze │ -> │ Process │ -> │ Reflect │ -> │ Iterate │
    └─────────┘    └─────────┘    └─────────┘    └─────────┘
          ^                                            |
          |                                            |
          └────────────────────────────────────────────┘
    """)
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║                 OPERATIONAL SEMANTICS PROJECT                ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝

    Cognitive Continuation Diagram:

    ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
    │ Analyze │ -> │ Process │ -> │ Reflect │ -> │ Iterate │
    └─────────┘    └─────────┘    └─────────┘    └─────────┘
          ^                                            |
          |                                            |
          └────────────────────────────────────────────┘
    """)

def check_dependencies():
    print_invariants()
    print("\nChecking dependencies...")
    dependencies = [
        ("hy", "Hy"),
        ("exa_py", "exa_py"),
        ("openai", "openai"),
        ("ripser", "ripser"),
        ("lambeq", "lambeq"),
        ("duckdb", "duckdb"),
        ("networkx", "networkx"),
    ]
    
    for module, name in dependencies:
        try:
            __import__(module)
            print(f"{name} is available.")
        except ImportError:
            print(f"Error: {name} is not installed. Please install it using 'pip install {module}'.")
            sys.exit(1)

    try:
        import subprocess
        result = subprocess.run(["bb", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Babashka is available. Version: {result.stdout.strip()}")
        else:
            raise FileNotFoundError
    except FileNotFoundError:
        print("Error: Babashka is not installed or not in the system PATH.")
        print("Please install Babashka and ensure it's in your system PATH.")
        sys.exit(1)

def run_tests():
    loader = unittest.TestLoader()
    start_dir = 'tests'
    suite = loader.discover(start_dir, pattern="test_*.py")
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

def run_all_analyses():
    print("\nRunning Ripser and lambeq integration analysis...")
    run_ripser_lambeq()
    
    print("\nEmbedding markdown files...")
    embed_markdown()
    
    print("\nAnalyzing topos directory structure...")
    analyze_topos()
    
    print("\nPrinting git statistics...")
    print_git_stats()
    
    print("\nPerforming concurrent random walks...")
    concurrent_random_walks()
    
    print("\nDiscovering package methods...")
    discover_package_methods()
    
    print("\nOptimizing storage...")
    optimize_storage('.')

if __name__ == "__main__":
    print_chapter_header()
    print("Checking dependencies...")
    check_dependencies()
    print("\nRunning tests...")
    run_tests()
    print("\nRunning quantum supermap tests...")
    run_quantum_tests()
    print("\nEnumerating files in the current working directory...")
    files = enumerate_files()
    print("Files found:")
    for file in files:
        print(f"- {file}")
    print("\nDemonstrating actegories...")
    act1 = Actegory("Actegory1")
    act1.add_object("A", 1)
    act1.add_object("B", 2)
    act1.add_morphism("f", lambda x: x + 1)
    act1.add_morphism("g", lambda x: x * 2)
    act2 = Actegory("Actegory2")
    actegory_functor(act1, act2, {"A": "X", "B": "Y"}, {"f": "h", "g": "k"})
    print(f"Actegory1 objects: {act1.objects}")
    print(f"Actegory1 morphisms: {list(act1.morphisms.keys())}")
    print(f"Actegory2 objects: {act2.objects}")
    print(f"Actegory2 morphisms: {list(act2.morphisms.keys())}")
    composed = act1.compose("f", "g")
    print(f"Composition result: {composed(3)}")
    print("\nExploring OpenAI API Action Space...")
    explore_action_space()
    print("\nRunning all analyses...")
    run_all_analyses()
    print("\nAnalyzing git complexity...")
    analyze_git_complexity()
    print("\nStarting NATS Knowledge Mutator...")
    mutator = NATSKnowledgeMutator("nats://localhost:4222", "nonlocal.info")
    asyncio.run(mutator.run())
    print("\nTests and analyses completed. Starting main program...")
    hy_main()
    
    print("\nAnalyzing screenshots on the desktop...")
    desktop_path = "/Users/barton/Desktop"
    analyze_screenshots_in_directory(desktop_path)

    print("\nStarting eventually consistent loop for screenshot analysis...")
    asyncio.run(eventually_consistent_loop())

    print("\nSummarizing project concepts and invariants...")
    summarize_project_concepts()

    print("\nRunning ACSets.jl analysis...")
    run_acsets_analysis()

    print("\nProgram execution completed. Please refer to README.md for more information.")
    print("\nTo run the Hy REPL with the core loop loaded, use the command: just hy-repl")
    print("\nTo run the Babashka-Hy REPL, use the command: just babashka-hy-repl")

