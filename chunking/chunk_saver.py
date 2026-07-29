import json
from pathlib import Path


class ChunkSaver:

    def save_chunks(self, chunks, metadata, output_file):

        output = []

        for idx, chunk in enumerate(chunks, start=1):

            output.append({
                "chunk_id": idx,
                "text": chunk,
                "metadata": metadata
            })

        Path(output_file).parent.mkdir(parents=True, exist_ok=True)

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=4, ensure_ascii=False)

        print(f"Saved {len(output)} chunks -> {output_file}")