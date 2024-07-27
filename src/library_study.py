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
    
    # Basic objects and morphisms
    x, y, z = discopy.Ob('x'), discopy.Ob('y'), discopy.Ob('z')
    f, g = discopy.Box('f', x, y), discopy.Box('g', y, z)
    print(f"Composition of morphisms: {g @ f}")
    
    # Creating a simple diagram
    diagram = discopy.Diagram.id(x) >> f >> g
    print(f"Simple diagram: {diagram}")
    
    # Using from_tuple method
    tuple_diagram = discopy.Diagram.from_tuple((x, y, z), (f, g))
    print(f"Diagram from tuple: {tuple_diagram}")
    
    # Creating a monoidal product of diagrams
    h = discopy.Box('h', x, z)
    product_diagram = diagram @ h
    print(f"Monoidal product of diagrams: {product_diagram}")
    
    # Using dagger (adjoint) method
    dagger_diagram = diagram.dagger()
    print(f"Dagger of diagram: {dagger_diagram}")
    
    # Creating a braided diagram
    braiding = discopy.Diagram.braid(x, y)
    braided_diagram = braiding >> (f @ discopy.Diagram.id(x))
    print(f"Braided diagram: {braided_diagram}")
    
    # Using cups and caps for compact closed structure
    cup = discopy.Diagram.cup(x, x.r)
    cap = discopy.Diagram.cap(x.l, x)
    snake_diagram = (discopy.Diagram.id(x) @ cup) >> (cap @ discopy.Diagram.id(x))
    print(f"Snake diagram (cup-cap composition): {snake_diagram}")
    
    # Creating a tensor diagram
    tensor = discopy.Tensor.cups(x, y)
    print(f"Tensor diagram: {tensor}")
    
    # Using the PRO (Progressive Rigid Operad) structure
    pro_diagram = discopy.PRO.permutation(3, 3)
    print(f"PRO diagram: {pro_diagram}")
    
    # Creating a traced diagram
    traced_diagram = discopy.Diagram.trace(diagram, x, y)
    print(f"Traced diagram: {traced_diagram}")
    
    # Using the Functor class for diagram rewriting
    F = discopy.Functor({x: y, y: z, z: x}, {f: g, g: h})
    rewritten_diagram = F(diagram)
    print(f"Rewritten diagram using Functor: {rewritten_diagram}")

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
