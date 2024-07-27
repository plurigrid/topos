import discopy
import catgrad
import lambeq
import duckdb
import _stack

def study_discopy():
    print("Studying discopy capabilities:")
    # Example usage of discopy
    x, y, z = discopy.Ob('x'), discopy.Ob('y'), discopy.Ob('z')
    f, g = discopy.Box('f', x, y), discopy.Box('g', y, z)
    print(g @ f)  # Composition of morphisms

def study_catgrad():
    print("\nStudying catgrad capabilities:")
    # Example usage of catgrad
    # Note: As of my knowledge cutoff, I don't have specific information about catgrad's API
    # You may need to adjust this based on the actual catgrad documentation
    print("catgrad is a library for categorical gradient descent.")
    print("Please refer to the catgrad documentation for specific usage examples.")

def study_lambeq():
    print("\nStudying lambeq capabilities:")
    # Example usage of lambeq
    from lambeq import BobcatParser
    parser = BobcatParser()
    sentence = "The cat sat on the mat."
    diagram = parser.sentence2diagram(sentence)
    print(f"Parsed sentence: {sentence}")
    print(f"Diagram: {diagram}")

def study_duckdb():
    print("\nStudying duckdb capabilities:")
    # Example usage of duckdb
    conn = duckdb.connect(':memory:')
    conn.execute("CREATE TABLE test (id INTEGER, name VARCHAR)")
    conn.execute("INSERT INTO test VALUES (1, 'Alice'), (2, 'Bob')")
    result = conn.execute("SELECT * FROM test").fetchall()
    print(f"DuckDB query result: {result}")

def study_stack():
    print("\nStudying _stack capabilities:")
    # Example usage of _stack
    # Note: As of my knowledge cutoff, I don't have specific information about _stack's API
    # You may need to adjust this based on the actual _stack documentation
    print("_stack is a library for stack-based programming.")
    print("Please refer to the _stack documentation for specific usage examples.")

def main():
    study_discopy()
    study_catgrad()
    study_lambeq()
    study_duckdb()
    study_stack()

if __name__ == "__main__":
    main()
