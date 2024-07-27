# Invariants about our current context

INVARIANTS = [
    "The project combines multiple programming paradigms: Python, Hy, and Babashka (Clojure)",
    "The project structure includes a main loop, file operations, library studies, and higher-order operads",
    "There's a focus on operational semantics and category theory concepts",
    "The project uses a Justfile for task management",
    "There's integration of various libraries: discopy, catgrad, lambeq, duckdb, _stack, exa_py, and ripser",
    "The project includes a filesystem analyzer and a random walk utility",
    "There's a Babashka-Hy REPL integration",
    "The project explores concepts like cognitive continuity and trust bandwidth maximization",
    "There's a focus on exasperated actions for various aspirations (VSA, ACSet, cognitive topology, etc.)",
    "The project includes test cases for file operations",
    "There's a reflexive evolving graph structure for analyzing the topos directory",
    "The project uses NetworkX for graph analysis",
    "The main program checks for dependencies before execution",
]

def print_invariants():
    print("Current context invariants:")
    for i, invariant in enumerate(INVARIANTS, 1):
        print(f"{i}. {invariant}")

if __name__ == "__main__":
    print_invariants()
