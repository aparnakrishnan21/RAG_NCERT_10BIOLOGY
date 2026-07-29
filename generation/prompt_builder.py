class PromptBuilder:
    """
    Builds prompts for the LLM using
    retrieved context + user question.
    """

    def __init__(self):
       self.system_instruction = (
    "You are an AI assistant answering questions using the provided context.\n\n"
    "Use only the information available in the context.\n"
    "If the answer requires combining information from multiple chunks, do so.\n"
    "If only part of the answer is available, answer with the available information.\n"
    "Only say 'I couldn't find the answer in the provided documents.' if the context contains no relevant information at all."
)

    def build(self, question, retrieved_chunks):
        """
        Parameters
        ----------
        question : str

        retrieved_chunks : list
            List of reranked chunk dictionaries.

        Returns
        -------
        str
        """

        context = ""

        for i, chunk in enumerate(retrieved_chunks, start=1):

            metadata = chunk.get("metadata", {})

            source = metadata.get("source", "Unknown")
            chapter = metadata.get("chapter_title", "Unknown")
            text = chunk.get("text", "")

            context += (
                f"[Chunk {i}]\n"
                f"Source: {source}\n"
                f"Chapter: {chapter}\n"
                f"{text}\n\n"
            )

        prompt = f"""
{self.system_instruction}

Context:
--------------------
{context}
--------------------

Question:
{question}

Answer:
"""

        return prompt.strip()