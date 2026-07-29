from sentence_transformers import SentenceTransformer


class EmbeddingGenerator:

    def __init__(self,
                 model_name="sentence-transformers/all-MiniLM-L6-v2"):

        self.model = SentenceTransformer(model_name)

    def generate_embedding(self, text):
        """
        Generate embedding for a single text chunk.
        """
        embedding = self.model.encode(
            text,
            convert_to_numpy=True
        )

        return embedding.tolist()

    def generate_embeddings(self, chunks):
        """
        Generate embeddings for multiple chunks.
        """
        results = []

        for chunk in chunks:

            embedding = self.generate_embedding(chunk["text"])

            results.append({
                "chunk_id": chunk["chunk_id"],
                "text": chunk["text"],
                "metadata": chunk["metadata"],
                "embedding": embedding
            })

        return results