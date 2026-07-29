from retrieval.bm25_retriever import BM25Retriever

retriever = BM25Retriever()

query = "What is photosynthesis?"

results = retriever.search(query)

for i, result in enumerate(results, start=1):

    print("=" * 60)
    print(f"Rank: {i}")
    print(f"Score: {result['score']:.4f}")
    print(f"Chunk ID: {result['id']}")
    print(result["metadata"])
    print()
    print(result["text"])
    print()