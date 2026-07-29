from generation.prompt_builder import PromptBuilder

chunks = [
    {
        "text": "Photosynthesis is the process by which green plants prepare food.",
        "source": "ncert_biology.pdf",
        "chapter_title": "Life Processes"
    },
    {
        "text": "Chlorophyll absorbs sunlight required for photosynthesis.",
        "source": "ncert_biology.pdf",
        "chapter_title": "Life Processes"
    }
]

builder = PromptBuilder()

prompt = builder.build(
    question="What is photosynthesis?",
    retrieved_chunks=chunks
)

print(prompt)