# Project Name

This project demonstrates various file operations, library studies, filesystem analysis, and exploration of higher-order operads.

## Getting Started

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the main program:
   ```
   python src/main.py
   ```

## Features

- File operations (list, read, write, copy, move, delete)
- Library capability studies (discopy, catgrad, lambeq, duckdb, _stack)
- Filesystem structure analysis
- Exploration of higher-order operads

## Project Structure

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
  ├── docs/
  │   └── README.md
  ├── .gitignore
  ├── requirements.txt
  ├── Justfile
  └── filesystem_structure.xml
```

## Running Tests

Tests are automatically run when you execute `src/main.py`. You can also run them separately using:

```
python -m unittest discover tests
```

## Using the Justfile

This project includes a Justfile for easy execution of common tasks. To use it, make sure you have `just` installed. Then you can run:

- `just install`: Install required dependencies
- `just run`: Run the main program
- `just study-libraries`: Study library capabilities
- `just analyze-filesystem`: Analyze filesystem structure
- `just explore-operads`: Explore higher-order operads
- `just test`: Run tests
- `just setup`: Setup the project and run all components
- `just instructions`: Display instructions for arriving at this level of operational semantics

For more information on each component, refer to the individual source files in the `src/` directory.
