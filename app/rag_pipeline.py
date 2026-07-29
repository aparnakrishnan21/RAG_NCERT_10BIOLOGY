# from retrieval.hybrid_retriever import HybridRetriever
# from retrieval.reranker import Reranker

# from generation.prompt_builder import PromptBuilder
# from generation.groq_generator import GroqGenerator


# def main():

#     print("=" * 60)
#     print("Hybrid RAG System")
#     print("=" * 60)

#     hybrid = HybridRetriever()

#     reranker = Reranker()

#     prompt_builder = PromptBuilder()

#     generator = GroqGenerator()

#     while True:

#         question = input("\nAsk a question (or type 'exit'): ")

#         if question.lower() == "exit":
#             print("Goodbye!")
#             break

#         print("\nSearching...")

#         retrieved = hybrid.search(
#             query=question,
#             top_k=10
#         )

#         print(f"Retrieved {len(retrieved)} chunks.")

#         print("Reranking...")

#         top_chunks = reranker.rerank(
#             query=question,
#             retrieved_chunks=retrieved,
#             top_k=5
#         )
#         # print("\n" + "=" * 70) 
#         # print("TOP CHUNKS")
#         # print("=" * 70)

#         # for i, chunk in enumerate(top_chunks, start=1):
#         #     print(f"\nChunk {i}")
#         #     print("Source:", chunk["metadata"]["source"])
#         #     print("Chapter:", chunk["metadata"]["chapter_title"])
#         #     print("-" * 50)
#         #     print(chunk["text"][:500])

#         print(f"Top {len(top_chunks)} chunks selected.")

#         print("Building prompt...")

#         prompt = prompt_builder.build(
#             question=question,
#             retrieved_chunks=top_chunks
#         )

#         print("Generating answer from Groq...\n")

#         answer = generator.generate(prompt)

#         print("=" * 60)
#         print("ANSWER")
#         print("=" * 60)
#         print(answer)


# if __name__ == "__main__":
#     main()

from retrieval.hybrid_retriever import HybridRetriever
from retrieval.reranker import Reranker
from generation.prompt_builder import PromptBuilder
from generation.groq_generator import GroqGenerator


# Initialize once
hybrid = HybridRetriever()
reranker = Reranker()
prompt_builder = PromptBuilder()
generator = GroqGenerator()


def ask_question(question: str) -> str:
    retrieved_chunks = hybrid.search(
        query=question,
        top_k=10
    )

    top_chunks = reranker.rerank(
        query=question,
        retrieved_chunks=retrieved_chunks,
        top_k=5
    )

    prompt = prompt_builder.build(
        question=question,
        retrieved_chunks=top_chunks
    )

    answer = generator.generate(prompt)

    return answer