import importlib
import random
from typing import List, Tuple

def get_package_methods(package_name: str, max_methods: int = 3) -> List[Tuple[str, str]]:
    """
    Get a list of methods from a package.
    
    :param package_name: Name of the package to explore
    :param max_methods: Maximum number of methods to return
    :return: List of tuples containing (method_name, method_docstring)
    """
    try:
        package = importlib.import_module(package_name)
        methods = []
        for name in dir(package):
            if not name.startswith('_'):
                attr = getattr(package, name)
                if callable(attr):
                    docstring = attr.__doc__ or "No docstring available"
                    methods.append((name, docstring.split('\n')[0]))
        return random.sample(methods, min(max_methods, len(methods)))
    except ImportError:
        print(f"Failed to import {package_name}")
        return []
    except Exception as e:
        print(f"Error exploring {package_name}: {str(e)}")
        return []

def discover_package_methods():
    """Discover methods of packages in dependencies."""
    packages = ['discopy', 'catgrad', 'lambeq', 'duckdb', '_stack']
    for package in packages:
        print(f"\nDiscovering methods in {package}:")
        methods = get_package_methods(package)
        for name, docstring in methods:
            print(f"  - {name}: {docstring}")

if __name__ == "__main__":
    discover_package_methods()
