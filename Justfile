# Variables
TOPOS_REMOTE := "git@github.com:plurigrid/topos.git"
PRETOPOS_REMOTE := "git@github.com:plurigrid/pretopos.git"
CURRENT_REPO_REMOTE := "git@github.com:bmorphism/pretopos.git"

# Default recipe (runs when just is called without arguments)
default:
    @just --list

# Git-related tasks
add-topos-remote:
    git remote add topos {{TOPOS_REMOTE}}

add-pretopos-remote:
    git remote add pretopos {{PRETOPOS_REMOTE}}

fetch-topos:
    git fetch topos

fetch-pretopos:
    git fetch pretopos

merge-topos:
    git merge topos/main

merge-pretopos:
    git merge pretopos/main

push-pretopos:
    git push {{CURRENT_REPO_REMOTE}} main

# Compositional merge task
compositional-merge: add-topos-remote add-pretopos-remote fetch-topos fetch-pretopos merge-topos merge-pretopos
    @echo "Compositional merge completed."

# Enumerate actions using 'say' command
enumerate-actions:
    @for action in $(just --summary); do \
        say "Action: $action"; \
        sleep 1; \
    done

# ASCII art map of pretopos-related actions
show-pretopos-map:
    @echo "
    +----------------+
    |   Pretopos     |
    |    Actions     |
    +----------------+
           |
           v
    +--------------+     +--------------+
    | Add Remotes  | --> | Fetch Remote |
    +--------------+     +--------------+
           |                    |
           v                    v
    +--------------+     +--------------+
    | Merge Remote | <-- | Push to Repo |
    +--------------+     +--------------+
           |
           v
    +--------------+
    | Compositional|
    |    Merge     |
    +--------------+
    "

# Run all analyses
run-analyses:
    python src/main.py

# Run tests
run-tests:
    python -m unittest discover tests

# Install dependencies
install-deps:
    pip install -r requirements.txt

# Clean up temporary files
clean:
    find . -type f -name "*.pyc" -delete
    find . -type d -name "__pycache__" -delete

# Generate project documentation
generate-docs:
    pdoc --html --output-dir docs src

# Run linter
lint:
    flake8 src tests

# Format code
format:
    black src tests

# Build project
build: install-deps lint format run-tests
    @echo "Build completed successfully."

# Deploy project (placeholder, customize as needed)
deploy: build
    @echo "Deploying project..."
    # Add your deployment steps here

# Update project
update: fetch-topos fetch-pretopos merge-topos merge-pretopos
    @echo "Project updated with latest changes from remotes."

# Start development environment
dev:
    @echo "Starting development environment..."
    # Add commands to start your development setup (e.g., launching editors, starting servers)

# Generate a new component (customize as needed)
generate-component name:
    @echo "Generating new component: {{name}}"
    mkdir -p src/components/{{name}}
    touch src/components/{{name}}/__init__.py
    touch src/components/{{name}}/{{name}}.py
    touch tests/components/test_{{name}}.py

# Run security audit
security-audit:
    safety check

# Backup project
backup:
    @echo "Backing up project..."
    tar -czf backup-$(date +%Y%m%d%H%M%S).tar.gz src tests requirements.txt Justfile

# Show project stats
project-stats:
    @echo "Project Statistics:"
    @echo "Total Python files: $(find src tests -name '*.py' | wc -l)"
    @echo "Total lines of code: $(find src tests -name '*.py' | xargs cat | wc -l)"
    @echo "Git commits: $(git rev-list --count HEAD)"
    @echo "Contributors: $(git shortlog -sn --no-merges | wc -l)"

# Help
help:
    @echo "Available recipes:"
    @just --list

echo ##active_line2##
# Metacognitive interaction with prioritized files
echo ##active_line3##
metacognitive-engage:
echo ##active_line4##
    @echo 'Engaging metacognitively with prioritized files...'
echo ##active_line5##
    @python utils/metacognition.py --files 'PK.lore.md capabilities_acset.jl clock.hy core_loop.hy pandoc_processor.py process_info.py push_to_repos.sh pyproject.toml run.py topos.pwd.csv __init__.py'
echo ##active_line6##

echo ##active_line7##
# Validate usage of exa_py tools
echo ##active_line8##
validate-exa-py:
echo ##active_line9##
    @echo 'Validating exa_py tool usage with files...'
echo ##active_line10##
    @python tools/exa_py_validator.py --files 'PK.lore.md capabilities_acset.jl clock.hy core_loop.hy pandoc_processor.py process_info.py push_to_repos.sh pyproject.toml run.py topos.pwd.csv __init__.py'
