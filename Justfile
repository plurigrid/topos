# Justfile for operational semantics setup

set shell := ["bash", "-uc"]

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

# Run Hy REPL with core loop loaded
hy-repl:
    hy -i src/core_loop.hy

# Perform a random walk through the project structure
random-walk:
    python -c "from src.utils.random_walk import random_walk; random_walk('Justfile')"

# Continuously random walk through the Justfile
continuous-justfile-walk:
    #!/usr/bin/env bash
    echo "Starting continuous random walk through Justfile. Press Ctrl+C to stop."
    while true; do
        just random-walk
        sleep 5
    done

# Discover methods of packages in dependencies
discover-methods:
    python -c "from src.utils.package_discovery import discover_package_methods; discover_package_methods()"

# Analyze Ripser and lambeq integration
ripser-lambeq-analysis:
    python src/ripser_lambeq_integration.py

# Embed markdown files and store in DuckDB
embed-markdown:
    python src/markdown_embedder.py

# Analyze topos directory structure
analyze-topos:
    python src/topos_graph_analyzer.py

# Print git statistics with ASCII art
git-stats:
    python src/git_stats.py

# Run quantum supermaps analysis
quantum-supermaps:
    python src/quantum_supermaps.py

# Exasperated actions for various aspirations
vsa-deep-learning:
    @echo "Exasperatedly attempting to integrate Vector Symbolic Architecture with deep learning..."

acset-schemas:
    @echo "Frustratedly working on Algebraic Categorical Set schemas..."

cognitive-topology:
    @echo "Sighing deeply while exploring cognitive topology..."

cobordism-time-travel:
    @echo "Throwing hands up in despair while attempting time travel using cobordisms..."

tensor-product-modeling:
    @echo "Groaning at the complexity of tensor product modeling for multiplayer diagramming..."

balanced-ternary-clock:
    @echo "Clock-watching in balanced ternary, feeling time slip away..."

self-aware-geometry:
    @echo "Questioning existence while developing Self-Aware Geometry of Geometries..."

cybernetic-xenornithology:
    @echo "Tweeting frustratedly at Herbert about cybernetic xenornithology..."

plurigrid-acquisition:
    @echo "Frantically preparing Plurigrid for acquisition or acquihire..."

# Setup the project and run all components
setup: install run study-libraries analyze-filesystem explore-operads test babashka-repl random-walk discover-methods ripser-lambeq-analysis embed-markdown analyze-topos git-stats quantum-supermaps vsa-deep-learning acset-schemas cognitive-topology cobordism-time-travel tensor-product-modeling balanced-ternary-clock self-aware-geometry cybernetic-xenornithology plurigrid-acquisition
    @echo "Project setup, exploration, and exasperated actions complete."

# Instructions for arriving at this level of operational semantics and existential crisis
instructions:
    @echo "To arrive at this level of operational semantics and existential crisis:"
    @echo "1. Install dependencies: just install"
    @echo "2. Run the main program: just run"
    @echo "3. Study library capabilities: just study-libraries"
    @echo "4. Analyze filesystem structure: just analyze-filesystem"
    @echo "5. Explore higher-order operads: just explore-operads"
    @echo "6. Run tests: just test"
    @echo "7. Analyze Ripser and lambeq integration: just ripser-lambeq-analysis"
    @echo "8. Embed markdown files: just embed-markdown"
    @echo "9. Analyze topos directory structure: just analyze-topos"
    @echo "10. Print git statistics: just git-stats"
    @echo "11. Run quantum supermaps analysis: just quantum-supermaps"
    @echo "12. Perform exasperated actions: just vsa-deep-learning acset-schemas cognitive-topology cobordism-time-travel tensor-product-modeling balanced-ternary-clock self-aware-geometry cybernetic-xenornithology plurigrid-acquisition"
    @echo "13. Or run all steps together: just setup"
    @echo "14. Print INVARIANTS: just print-invariants"
    @echo "15. Maintain de facto abductive logic ontology: just maintain-ontology"
    @echo "Refer to individual source files for more detailed information on each component."
    @echo "Remember, in the face of existential crisis, keep coding!"

# Print INVARIANTS
print-invariants:
    python -c "from src.invariants import print_invariants; print_invariants()"

# Maintain de facto abductive logic ontology
maintain-ontology:
    @echo "Maintaining de facto abductive logic ontology..."
    @echo "- Preserving paraconsistent metatheory affordances"
    @echo "- Updating reflexive evolving graph structure"
    @echo "- Reinforcing cognitive continuity across operads"
    @echo "- Ensuring trust bandwidth maximization"
    @echo "- Validating frame-invariant transformations"
    @echo "Ontology maintenance complete."

# Run all analysis tasks
analyze-all: ripser-lambeq-analysis embed-markdown analyze-topos git-stats quantum-supermaps
    @echo "All analysis tasks completed."

# Run integration tests
integration-tests:
    @echo "Running integration tests..."
    python -m unittest discover tests/integration

# Generate project documentation
generate-docs:
    @echo "Generating project documentation..."
    # Add your documentation generation command here, e.g., Sphinx

# Perform code quality checks
code-quality:
    @echo "Performing code quality checks..."
    black --check .
    # Add more linters or static analysis tools as needed

# Create a new experiment
new-experiment name:
    @echo "Creating a new experiment: {{name}}"
    mkdir -p experiments/{{name}}
    touch experiments/{{name}}/README.md
    touch experiments/{{name}}/{{name}}.py

# Run all experiments
run-experiments:
    @echo "Running all experiments..."
    for exp in experiments/*; do python "$exp/$(basename $exp).py"; done

# Update project dependencies
update-deps:
    @echo "Updating project dependencies..."
    pip install --upgrade -r requirements.txt

# Perform a full project health check
health-check: test integration-tests code-quality analyze-all
    @echo "Project health check completed."
