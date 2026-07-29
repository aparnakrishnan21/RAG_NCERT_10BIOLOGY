from retrieval.hybrid_retriever import HybridRetriever
from retrieval.reranker import Reranker


hybrid = HybridRetriever()

reranker = Reranker()

query = "What is photosynthesis?"

results = hybrid.search(query)

reranked = reranker.rerank(query, results)

for i, result in enumerate(reranked, start=1):

    print("=" * 60)
    print(f"Rank: {i}")
    print(f"Chunk ID: {result['id']}")
    print(f"Rerank Score: {result['rerank_score']:.4f}")
    print(result["metadata"])
    print()
    print(result["text"])
    print()