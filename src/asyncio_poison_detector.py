import ast
import asyncio
from typing import List, Tuple
import black

def detect_asyncio_poison(file_path: str) -> List[Tuple[int, str]]:
    """
    Detect potential asyncio poison in a Python file.
    
    :param file_path: Path to the Python file to analyze
    :return: List of tuples containing line numbers and descriptions of potential asyncio poison
    """
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Use black to format the code
    try:
        formatted_content = black.format_str(content, mode=black.FileMode())
    except black.InvalidInput:
        return [(0, "Unable to parse the file with black")]

    tree = ast.parse(formatted_content)
    issues = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == 'run_until_complete':
            issues.append((node.lineno, "Use of run_until_complete() can lead to asyncio poison"))
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr == 'run_until_complete':
                issues.append((node.lineno, "Use of run_until_complete() can lead to asyncio poison"))
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'sleep':
            issues.append((node.lineno, "Use of time.sleep() in asyncio context can lead to blocking"))

    return issues

def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: python asyncio_poison_detector.py <file_path>")
        return

    file_path = sys.argv[1]
    issues = detect_asyncio_poison(file_path)

    if issues:
        print(f"Potential asyncio poison detected in {file_path}:")
        for line, description in issues:
            print(f"Line {line}: {description}")
    else:
        print(f"No potential asyncio poison detected in {file_path}")

if __name__ == "__main__":
    main()
