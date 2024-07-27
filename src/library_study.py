import discopy
import catgrad
import lambeq
import duckdb
import _stack
import traceback

def safe_execute(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(f"Error in {func.__name__}: {str(e)}")
            print(traceback.format_exc())
    return wrapper

@safe_execute
def study_discopy():
    print("Studying discopy capabilities:")
    x, y, z = discopy.Ob('x'), discopy.Ob('y'), discopy.Ob('z')
    f, g = discopy.Box('f', x, y), discopy.Box('g', y, z)
    print(f"Composition of morphisms: {g @ f}")
    
    # Additional example: Creating a simple diagram
    diagram = discopy.Diagram.id(x) >> f >> g
    print(f"Simple diagram: {diagram}")

@safe_execute
def study_catgrad():
    print("\nStudying catgrad capabilities:")
    print("catgrad is a library for categorical gradient descent.")
    # As catgrad's API is not well-known, we'll provide a hypothetical example
    print("Hypothetical example:")
    print("gradient = catgrad.compute_gradient(function, input)")
    print("optimized_value = catgrad.optimize(function, initial_value, steps=100)")

@safe_execute
def study_lambeq():
    print("\nStudying lambeq capabilities:")
    from lambeq import BobcatParser, AtomicType, IQPAnsatz
    
    parser = BobcatParser()
    sentence = "The cat sat on the mat."
    diagram = parser.sentence2diagram(sentence)
    print(f"Parsed sentence: {sentence}")
    print(f"Diagram: {diagram}")
    
    # Additional example: Creating a simple circuit
    s, n = AtomicType.SENTENCE, AtomicType.NOUN
    circuit = IQPAnsatz().apply(diagram)
    print(f"Circuit from diagram: {circuit}")

@safe_execute
def study_duckdb():
    print("\nStudying duckdb capabilities:")
    conn = duckdb.connect(':memory:')
    conn.execute("CREATE TABLE test (id INTEGER, name VARCHAR)")
    conn.execute("INSERT INTO test VALUES (1, 'Alice'), (2, 'Bob'), (3, 'Charlie')")
    result = conn.execute("SELECT * FROM test ORDER BY id").fetchall()
    print(f"DuckDB query result: {result}")
    
    # Additional example: Aggregation
    agg_result = conn.execute("SELECT COUNT(*) as count, AVG(id) as avg_id FROM test").fetchone()
    print(f"Aggregation result: Count = {agg_result[0]}, Average ID = {agg_result[1]}")

@safe_execute
def study_stack():
    print("\nStudying _stack capabilities:")
    print("_stack is a library for stack-based programming.")
    # As _stack's API is not well-known, we'll provide a hypothetical example
    print("Hypothetical example:")
    print("stack = _stack.Stack()")
    print("stack.push(5)")
    print("stack.push(3)")
    print("result = stack.pop() + stack.pop()")
    print("print(result)  # Output: 8")

def main():
    study_discopy()
    study_catgrad()
    study_lambeq()
    study_duckdb()
    study_stack()

if __name__ == "__main__":
    main()
