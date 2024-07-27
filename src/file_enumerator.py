import os

def enumerate_files():
    likely_files = [
        'README.md',
        'requirements.txt',
        'setup.py',
        'main.py',
        'Justfile',
        '.gitignore',
        'src/main.py',
        'src/core_loop.hy',
        'src/filesystem_analyzer.py',
        'src/higher_order_operads.py',
        'src/library_study.py',
        'src/utils/file_ops.py',
        'tests/test_main.py',
        'filesystem_structure.xml',
        'main.bb',
        'src/invariants.py',
        'src/topos_graph_analyzer.py',
        'src/quantum_supermaps.py',
        'src/modal_julia_app.py',
        'src/julia_exploration.jl',
        'setup_dit.py',
        'how_we_work.md',
        'INVARIANTS'
    ]

    existing_files = []
    for file in likely_files:
        if os.path.exists(file):
            existing_files.append(file)

    return existing_files

if __name__ == "__main__":
    files = enumerate_files()
    print("Files found in the current working directory:")
    for file in files:
        print(f"- {file}")
