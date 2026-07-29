import chromadb


class ChromaVectorDB:

    def __init__(
        self,
        db_path="data/vectordb",
        collection_name="ncert_biology"
    ):

        self.client = chromadb.PersistentClient(path=db_path)

        self.collection = self.client.get_or_create_collection(
            name=collection_name
        )

    def add_embeddings(self, embedded_chunks):

        ids = []
        embeddings = []
        documents = []
        metadatas = []

        for chunk in embedded_chunks:

            ids.append(str(chunk["chunk_id"]))

            embeddings.append(chunk["embedding"])

            documents.append(chunk["text"])

            metadatas.append({
    "chunk_id": chunk["chunk_id"],
    "source": chunk["metadata"]["source"],
    "chapter_number": str(chunk["metadata"]["chapter_number"]),
    "chapter_title": chunk["metadata"]["chapter_title"]
})

        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=documents,
            metadatas=metadatas
        )

    def search(self, query_embedding, top_k=5):

        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
