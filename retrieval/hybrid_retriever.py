from retrieval.dense_retriever import DenseRetriever
from retrieval.bm25_retriever import BM25Retriever


class HybridRetriever:

    def __init__(self):

        self.dense = DenseRetriever()
        self.bm25 = BM25Retriever()

    def search(self, query, top_k=5):

        dense_results = self.dense.search(query, top_k)

        bm25_results = self.bm25.search(query, top_k)

        fused_scores = {}

        # Dense Retrieval
        for rank, result in enumerate(dense_results):

            chunk_id = result["id"]

            fused_scores.setdefault(chunk_id, {
                "result": result,
                "score": 0
            })

            fused_scores[chunk_id]["score"] += 1 / (60 + rank + 1)

        # BM25 Retrieval
        for rank, result in enumerate(bm25_results):

            chunk_id = result["id"]

            if chunk_id not in fused_scores:

                fused_scores[chunk_id] = {
                    "result": result,
                    "score": 0
                }

            fused_scores[chunk_id]["score"] += 1 / (60 + rank + 1)

        results = sorted(
            fused_scores.values(),
            key=lambda x: x["score"],
            reverse=True
        )

        final_results = []

        for item in results[:top_k]:
            result = item["result"].copy()
            result["rrf_score"] = item["score"]
            final_results.append(result)

        return final_results