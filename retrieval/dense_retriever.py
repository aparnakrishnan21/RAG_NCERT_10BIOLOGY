# import chromadb
# from sentence_transformers import SentenceTransformer


# class DenseRetriever:
#     def __init__(
#         self,
#         db_path="data/vectordb",
#         collection_name="ncert_biology",
#         model_name="sentence-transformers/all-MiniLM-L6-v2",
#     ):
#         self.model = SentenceTransformer(model_name)

#         self.client = chromadb.PersistentClient(path=db_path)

#         self.collection = self.client.get_collection(collection_name)

#     def search(self, query, top_k=5):
#         query_embedding = self.model.encode(query).tolist()

#         results = self.collection.query(
#             query_embeddings=[query_embedding],
#             n_results=top_k,
#         )

#         return results




from sentence_transformers import SentenceTransformer
from vectordb.chromadb import ChromaVectorDB


class DenseRetriever:

    def __init__(self):
        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )
        self.db = ChromaVectorDB()

    def search(self, query, top_k=5):
        query_embedding = self.model.encode(query).tolist()

        results = self.db.search(query_embedding, top_k)

        retrieved = []

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]

        for doc, meta, distance in zip(documents, metadatas, distances):
            retrieved.append({
    "id": meta["chunk_id"],
    "text": doc,
    "metadata": {
        "source": meta["source"],
        "chapter_number": meta["chapter_number"],
        "chapter_title": meta["chapter_title"]
    },
    "score": distance
})
        return retrieved
    