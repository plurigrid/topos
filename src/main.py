import hy
import unittest
from core_loop import main

def run_tests():
    loader = unittest.TestLoader()
    start_dir = 'tests'
    suite = loader.discover(start_dir, pattern="test_*.py")
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    print("Running tests...")
    run_tests()
    print("\nTests completed. Starting main program...")
    main()
    print("\nProgram execution completed. Please refer to README.md for more information.")
    print("\nTo run the Babashka-Hy REPL, use the command: just babashka-hy-repl")
