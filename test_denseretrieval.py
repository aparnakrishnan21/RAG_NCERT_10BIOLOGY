# from retrieval.dense_retriever import DenseRetriever

# retriever = DenseRetriever()

# query = "What is photosynthesis?"

# results = retriever.search(query)

# documents = results["documents"][0]
# metadatas = results["metadatas"][0]
# distances = results["distances"][0]

# for i, (doc, meta, score) in enumerate(zip(documents, metadatas, distances), start=1):
#     print("=" * 60)
#     print(f"Rank: {i}")
#     print(f"Distance: {score:.4f}")
#     print(f"Metadata: {meta}")
#     print()
#     print(doc)
    # print()
from retrieval.dense_retriever import DenseRetriever

retriever = DenseRetriever()

query = "What is photosynthesis?"

results = retriever.search(query)

for i, result in enumerate(results, start=1):
    print("=" * 60)
    print(f"Rank: {i}")
    print(f"Distance: {result['score']:.4f}")
    print(f"Chunk ID: {result['id']}")
    print(f"Metadata: {result['metadata']}")
    print()
    print(result["text"])
    print()