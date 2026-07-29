import json
from pathlib import Path

from embeddings.embedder import EmbeddingGenerator


embedder = EmbeddingGenerator()

chunk_files = sorted(Path("data/chunks").glob("*_chunks.json"))

print(f"Found {len(chunk_files)} chunk file(s)\n")

for chunk_file in chunk_files:

    print("=" * 60)
    print(f"Processing: {chunk_file.name}")

    with open(chunk_file, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    embedded_chunks = embedder.generate_embeddings(chunks)

    output_path = (
        Path("data/embeddings") /
        chunk_file.name.replace("_chunks", "_embeddings")
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(
            embedded_chunks,
            f,
            indent=4
        )

    print(f"Saved embeddings -> {output_path}")
    print(f"Chunks embedded : {len(embedded_chunks)}\n")