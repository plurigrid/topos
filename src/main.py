import sys
import unittest
import asyncio
from core_loop import main
import exa_py
from invariants import print_invariants
from quantum_supermaps import run_tests as run_quantum_tests
from file_enumerator import enumerate_files
from actegories import Actegory, actegory_functor
from openai_api_handler import explore_action_space
from ripser_lambeq_integration import main as run_ripser_lambeq
from markdown_embedder import main as embed_markdown
from topos_graph_analyzer import main as analyze_topos
from git_stats import print_git_stats
from utils.random_walk import concurrent_random_walks
from utils.package_discovery import discover_package_methods
from storage_optimizer import optimize_storage
from nats_knowledge_mutator import NATSKnowledgeMutator

def print_chapter_header():
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
    print("\nStarting NATS Knowledge Mutator...")
    mutator = NATSKnowledgeMutator("nats://localhost:4222", "nonlocal.info")
    asyncio.run(mutator.run())
    print("\nTests and analyses completed. Starting main program...")
    main()
    print("\nProgram execution completed. Please refer to README.md for more information.")
    print("\nTo run the Babashka-Hy REPL, use the command: just babashka-hy-repl")

