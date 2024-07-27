import sys
import unittest
from core_loop import main
import exa_py
from invariants import print_invariants
from quantum_supermaps import run_tests as run_quantum_tests
from file_enumerator import enumerate_files
from actegories import Actegory, actegory_functor
from openai_api_handler import explore_action_space

def check_dependencies():
    print_invariants()
    print("\nChecking dependencies...")
    try:
        import hy
        print("Hy is available.")
    except ImportError:
        print("Error: Hy is not installed. Please install it using 'pip install hy'.")
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

    try:
        import exa_py
        print("exa_py is available.")
    except ImportError:
        print("Error: exa_py is not installed. Please install it using 'pip install exa_py'.")
        sys.exit(1)

    try:
        import openai
        print("openai is available.")
    except ImportError:
        print("Error: openai is not installed. Please install it using 'pip install openai'.")
        sys.exit(1)

def run_tests():
    loader = unittest.TestLoader()
    start_dir = 'tests'
    suite = loader.discover(start_dir, pattern="test_*.py")
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == "__main__":
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
    print("\nTests completed. Starting main program...")
    main()
    print("\nProgram execution completed. Please refer to README.md for more information.")
    print("\nTo run the Babashka-Hy REPL, use the command: just babashka-hy-repl")

