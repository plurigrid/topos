# Operational Semantics Project

This project demonstrates various aspects of operational semantics, including file operations, library studies, filesystem analysis, exploration of higher-order operads, and integration of Babashka and Hy.

## Getting Started

To reach the current level of understanding and functionality, follow these steps:

1. **Setup the Environment**
   - Install Python 3.x
   - Install Babashka (bb)
   - Install Hy
   - Install Just (command runner)

2. **Clone the Repository**
   ```
   git clone <repository-url>
   cd <repository-name>
   ```

3. **Install Dependencies**
   ```
   just install
   ```

4. **Explore Core Functionality**
   - Run the main program:
     ```
     just run
     ```
   - This will execute `src/main.py`, which includes running tests and the main program logic.

5. **Study Library Capabilities**
   ```
   just study-libraries
   ```
   This will run `src/library_study.py`, exploring capabilities of libraries like discopy, catgrad, lambeq, duckdb, and _stack.

6. **Analyze Filesystem Structure**
   ```
   just analyze-filesystem
   ```
   This executes `src/filesystem_analyzer.py`, which parses and analyzes the filesystem structure defined in `filesystem_structure.xml`.

7. **Explore Higher-Order Operads**
   ```
   just explore-operads
   ```
   This runs `src/higher_order_operads.py`, demonstrating concepts related to higher-order operads.

8. **Run Tests**
   ```
   just test
   ```
   This executes all tests in the `tests/` directory.

9. **Use the Babashka-Hy REPL**
   ```
   just babashka-repl
   ```
   This starts the Babashka REPL with Hy integration. You can:
   - Enter Babashka code directly
   - Prefix Hy code with "hy:" to execute Hy code
   - Type 'exit' to quit the REPL

10. **Review Project Structure**
    ```
    / (root)
      ├── src/
      │   ├── main.py
      │   ├── core_loop.hy
      │   ├── filesystem_analyzer.py
      │   ├── higher_order_operads.py
      │   ├── library_study.py
      │   └── utils/
      │       └── file_ops.py
      ├── tests/
      │   └── test_main.py
      ├── main.bb
      ├── requirements.txt
      ├── Justfile
      └── filesystem_structure.xml
    ```

11. **Understand Key Components**
    - `src/main.py`: Entry point, runs tests and main program
    - `src/core_loop.hy`: Core logic written in Hy
    - `src/filesystem_analyzer.py`: Analyzes filesystem structure
    - `src/higher_order_operads.py`: Explores higher-order operads
    - `src/library_study.py`: Studies various library capabilities
    - `src/utils/file_ops.py`: Utility functions for file operations
    - `main.bb`: Babashka script for REPL with Hy integration
    - `Justfile`: Contains commands for easy project management

## Using the Justfile

The project includes a Justfile for easy execution of common tasks:

- `just install`: Install required dependencies
- `just run`: Run the main program
- `just study-libraries`: Study library capabilities
- `just analyze-filesystem`: Analyze filesystem structure
- `just explore-operads`: Explore higher-order operads
- `just test`: Run tests
- `just babashka-repl`: Start the Babashka-Hy REPL
- `just setup`: Setup the project and run all components
- `just instructions`: Display these instructions

For more detailed information on each component, refer to the individual source files in the `src/` directory.
