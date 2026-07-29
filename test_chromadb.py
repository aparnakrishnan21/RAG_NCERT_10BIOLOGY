import json
from pathlib import Path

from vectordb.chromadb import ChromaVectorDB

db = ChromaVectorDB()

embedding_files = sorted(
    Path("data/embeddings").glob("*_embeddings.json")
)

print(f"Found {len(embedding_files)} embedding file(s)\n")

for file in embedding_files:

    print("=" * 60)
    print(f"Loading: {file.name}")

    with open(file, "r", encoding="utf-8") as f:
        embedded_chunks = json.load(f)

    db.add_embeddings(embedded_chunks)

    print(f"Inserted {len(embedded_chunks)} vectors\n")