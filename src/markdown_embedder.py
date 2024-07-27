import os
import duckdb
import openai
from typing import List, Tuple
import numpy as np

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def find_markdown_files(root_dir: str, max_depth: int = 11) -> List[str]:
    """Find all markdown files in the given directory up to the specified depth."""
    markdown_files = []
    for root, _, files in os.walk(root_dir):
        if root.count(os.sep) - root_dir.count(os.sep) >= max_depth:
            continue
        for file in files:
            if file.endswith('.md'):
                markdown_files.append(os.path.join(root, file))
    return markdown_files

def get_embedding(text: str) -> List[float]:
    """Get the embedding for the given text using OpenAI's best quality model."""
    response = openai.Embedding.create(
        input=text,
        model="text-embedding-ada-002"  # This is currently OpenAI's best quality embedding model
    )
    return response['data'][0]['embedding']

def embed_markdown_files(files: List[str]) -> List[Tuple[str, List[float]]]:
    """Embed the content of each markdown file."""
    embeddings = []
    for file in files:
        with open(file, 'r') as f:
            content = f.read()
        embedding = get_embedding(content)
        embeddings.append((file, embedding))
    return embeddings

def setup_duckdb(db_name: str = 'markdown_embeddings.db'):
    """Set up DuckDB with vector similarity search capabilities."""
    conn = duckdb.connect(db_name)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS markdown_embeddings (
            file_path VARCHAR,
            embedding FLOAT[]
        );
    """)
    conn.execute("CREATE INDEX IF NOT EXISTS embedding_index ON markdown_embeddings USING vss(embedding);")
    return conn

def store_embeddings(conn: duckdb.DuckDBPyConnection, embeddings: List[Tuple[str, List[float]]]):
    """Store the embeddings in DuckDB."""
    for file_path, embedding in embeddings:
        conn.execute("""
            INSERT INTO markdown_embeddings (file_path, embedding)
            VALUES (?, ?);
        """, (file_path, embedding))

def enable_matryoshka_embedding(conn: duckdb.DuckDBPyConnection):
    """Enable Matryoshka embedding in DuckDB."""
    conn.execute("SET vss_enable_matryoshka = true;")

def main():
    root_dir = '/Users/barton/topos'  # Adjust this to your project's root directory
    db_name = 'markdown_embeddings.db'

    print("Finding markdown files...")
    markdown_files = find_markdown_files(root_dir)
    print(f"Found {len(markdown_files)} markdown files.")

    print("Embedding markdown files...")
    embeddings = embed_markdown_files(markdown_files)
    print("Embedding complete.")

    print("Setting up DuckDB...")
    conn = setup_duckdb(db_name)
    
    print("Enabling Matryoshka embedding...")
    enable_matryoshka_embedding(conn)

    print("Storing embeddings in DuckDB...")
    store_embeddings(conn, embeddings)
    print("Embeddings stored successfully.")

    conn.close()
    print(f"Process complete. Embeddings stored in {db_name}")

if __name__ == "__main__":
    main()
