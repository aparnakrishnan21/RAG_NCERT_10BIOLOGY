import os
import json
import re
from rank_bm25 import BM25Okapi


class BM25Retriever:

    def __init__(self, chunks_folder="data/chunks"):

        self.documents = []
        self.tokenized_documents = []

        # Load all chunk files
        for file in os.listdir(chunks_folder):

            if file.endswith("_chunks.json"):

                filepath = os.path.join(chunks_folder, file)

                with open(filepath, "r", encoding="utf-8") as f:
                    chunks = json.load(f)

                for chunk in chunks:

                    self.documents.append(chunk)

                    tokens = self.tokenize(chunk["text"])
                    self.tokenized_documents.append(tokens)

        self.bm25 = BM25Okapi(self.tokenized_documents)

    def tokenize(self, text):
        return re.findall(r"\w+", text.lower())

    def search(self, query, top_k=5):

        query_tokens = self.tokenize(query)

        scores = self.bm25.get_scores(query_tokens)

        ranked = sorted(
            enumerate(scores),
            key=lambda x: x[1],
            reverse=True
        )

        results = []

        for idx, score in ranked[:top_k]:

            chunk = self.documents[idx]

            results.append({
    "id": chunk["chunk_id"],
    "text": chunk["text"],
    "metadata": chunk["metadata"],
    "score": score
})

        return results