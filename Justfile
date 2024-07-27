# Justfile for operational semantics setup

# Install required dependencies
install:
    pip install -r requirements.txt

# Run the main program
run:
    python src/main.py

# Study library capabilities
study-libraries:
    python -c "from src.library_study import main; main()"

# Analyze filesystem structure
analyze-filesystem:
    python -c "from src.filesystem_analyzer import main; main('filesystem_structure.xml')"

# Explore higher-order operads
explore-operads:
    python -c "from src.higher_order_operads import main; main()"

# Run tests
test:
    python -m unittest discover tests

# Run Babashka-Hy REPL
babashka-repl:
    bb main.bb

# Perform a random walk through the project structure
random-walk:
    python -c "from src.utils.random_walk import random_walk; random_walk()"

# Discover methods of packages in dependencies
discover-methods:
    python -c "from src.utils.package_discovery import discover_package_methods; discover_package_methods()"

# Setup the project and run all components
setup: install run study-libraries analyze-filesystem explore-operads test babashka-repl random-walk discover-methods
    @echo "Project setup and exploration complete."

# Instructions for arriving at this level of operational semantics
instructions:
    @echo "To arrive at this level of operational semantics:"
    @echo "1. Install dependencies: just install"
    @echo "2. Run the main program: just run"
    @echo "3. Study library capabilities: just study-libraries"
    @echo "4. Analyze filesystem structure: just analyze-filesystem"
    @echo "5. Explore higher-order operads: just explore-operads"
    @echo "6. Run tests: just test"
    @echo "7. Or run all steps together: just setup"
    @echo "Refer to individual source files for more detailed information on each component."
