from sentence_transformers import CrossEncoder


class Reranker:

    def __init__(
        self,
        model_name="cross-encoder/ms-marco-MiniLM-L-6-v2"
    ):

        self.model = CrossEncoder(model_name)

    def rerank(self, query, retrieved_chunks, top_k=3):

        pairs = []

        for chunk in retrieved_chunks:
            pairs.append((query, chunk["text"]))

        scores = self.model.predict(pairs)

        for chunk, score in zip(retrieved_chunks, scores):
            chunk["rerank_score"] = float(score)

        reranked = sorted(
            retrieved_chunks,
            key=lambda x: x["rerank_score"],
            reverse=True
        )

        return reranked[:top_k]