import importlib
import traceback
from functools import wraps

def safe_execute(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error in {func.__name__}: {str(e)}")
            print(traceback.format_exc())
    return wrapper

def import_library(library_name):
    try:
        return importlib.import_module(library_name)
    except ImportError:
        print(f"Failed to import {library_name}. Make sure it's installed.")
        return None
    except Exception as e:
        print(f"Unexpected error importing {library_name}: {e}")
        return None

@safe_execute
def study_discopy():
    discopy = import_library('discopy')
    if not discopy:
        return

    print("Studying discopy capabilities:")
    
    x, y, z = discopy.Ob('x'), discopy.Ob('y'), discopy.Ob('z')
    f, g = discopy.Box('f', x, y), discopy.Box('g', y, z)
    
    examples = [
        ("Composition of morphisms", lambda: g @ f),
        ("Simple diagram", lambda: discopy.Diagram.id(x) >> f >> g),
        ("Diagram from tuple", lambda: discopy.Diagram.from_tuple((x, y, z), (f, g))),
        ("Monoidal product of diagrams", lambda: (discopy.Diagram.id(x) >> f >> g) @ discopy.Box('h', x, z)),
        ("Dagger of diagram", lambda: (discopy.Diagram.id(x) >> f >> g).dagger()),
        ("Braided diagram", lambda: discopy.Diagram.braid(x, y) >> (f @ discopy.Diagram.id(x))),
        ("Snake diagram", lambda: (discopy.Diagram.id(x) @ discopy.Diagram.cup(x, x.r)) >> (discopy.Diagram.cap(x.l, x) @ discopy.Diagram.id(x))),
        ("Tensor diagram", lambda: discopy.Tensor.cups(x, y)),
        ("PRO diagram", lambda: discopy.PRO.permutation(3, 3)),
        ("Traced diagram", lambda: discopy.Diagram.trace(discopy.Diagram.id(x) >> f >> g, x, y)),
        ("Rewritten diagram using Functor", lambda: discopy.Functor({x: y, y: z, z: x}, {f: g, g: discopy.Box('h', x, z)})(discopy.Diagram.id(x) >> f >> g))
    ]

    for name, func in examples:
        try:
            result = func()
            print(f"{name}: {result}")
        except Exception as e:
            print(f"Error in {name}: {str(e)}")

@safe_execute
def study_catgrad():
    catgrad = import_library('catgrad')
    if not catgrad:
        return

    print("\nStudying catgrad capabilities:")
    print("catgrad is a library for categorical gradient descent.")
    # Add actual examples if the API becomes known

@safe_execute
def study_lambeq():
    lambeq = import_library('lambeq')
    if not lambeq:
        return

    print("\nStudying lambeq capabilities:")
    
    parser = lambeq.BobcatParser()
    sentence = "The cat sat on the mat."
    diagram = parser.sentence2diagram(sentence)
    print(f"Parsed sentence: {sentence}")
    print(f"Diagram: {diagram}")
    
    s, n = lambeq.AtomicType.SENTENCE, lambeq.AtomicType.NOUN
    circuit = lambeq.IQPAnsatz().apply(diagram)
    print(f"Circuit from diagram: {circuit}")

@safe_execute
def study_duckdb():
    duckdb = import_library('duckdb')
    if not duckdb:
        return

    print("\nStudying duckdb capabilities:")
    conn = duckdb.connect(':memory:')
    conn.execute("CREATE TABLE test (id INTEGER, name VARCHAR)")
    conn.execute("INSERT INTO test VALUES (1, 'Alice'), (2, 'Bob'), (3, 'Charlie')")
    result = conn.execute("SELECT * FROM test ORDER BY id").fetchall()
    print(f"DuckDB query result: {result}")
    
    agg_result = conn.execute("SELECT COUNT(*) as count, AVG(id) as avg_id FROM test").fetchone()
    print(f"Aggregation result: Count = {agg_result[0]}, Average ID = {agg_result[1]}")

@safe_execute
def study_stack():
    _stack = import_library('_stack')
    if not _stack:
        return

    print("\nStudying _stack capabilities:")
    print("_stack is a library for stack-based programming.")
    # Add actual examples if the API becomes known

def main():
    libraries = {
        "discopy": study_discopy,
        "catgrad": study_catgrad,
        "lambeq": study_lambeq,
        "duckdb": study_duckdb,
        "_stack": study_stack
    }
    for name, study_func in libraries.items():
        print(f"\nStudying {name} capabilities:")
        study_func()

if __name__ == "__main__":
    main()
