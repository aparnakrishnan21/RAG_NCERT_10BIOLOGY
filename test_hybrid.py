from retrieval.hybrid_retriever import HybridRetriever

retriever = HybridRetriever()

query = "What is photosynthesis?"

results = retriever.search(query)

for i, result in enumerate(results, start=1):

    print("=" * 60)
    print(f"Rank: {i}")
    print(f"Chunk ID: {result['id']}")
    print(f"RRF Score: {result['rrf_score']:.6f}")
    print(result["metadata"])
    print()
    print(result["text"])
    print()