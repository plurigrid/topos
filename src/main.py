import sys
import unittest
from core_loop import main
import exa_py

def check_dependencies():
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
    print("\nTests completed. Starting main program...")
    main()
    print("\nProgram execution completed. Please refer to README.md for more information.")
    print("\nTo run the Babashka-Hy REPL, use the command: just babashka-hy-repl")
