# from generation.prompt_builder import PromptBuilder
# from generation.groq_generator import GroqGenerator

# # Simulated retrieved chunks
# chunks = [
#     {
#         "text": "Photosynthesis is the process by which green plants prepare food using sunlight, carbon dioxide, and water.",
#         "source": "ncert_biology.pdf",
#         "chapter_title": "Life Processes"
#     },
#     {
#         "text": "Chlorophyll absorbs sunlight required for photosynthesis.",
#         "source": "ncert_biology.pdf",
#         "chapter_title": "Life Processes"
#     }
# ]

# question = "What is photosynthesis?"

# # Build prompt
# builder = PromptBuilder()
# prompt = builder.build(question, chunks)

# # Generate answer
# generator = GroqGenerator()
# answer = generator.generate(prompt)

# print("\n===== Generated Answer =====\n")
# print(answer)

from generation.prompt_builder import PromptBuilder
from generation.groq_generator import GroqGenerator


def test_rag_pipeline():
    chunks = [
        {
            "text": "Photosynthesis is the process by which green plants prepare food using sunlight, carbon dioxide, and water.",
            "source": "ncert_biology.pdf",
            "chapter_title": "Life Processes",
        },
        {
            "text": "Chlorophyll absorbs sunlight required for photosynthesis.",
            "source": "ncert_biology.pdf",
            "chapter_title": "Life Processes",
        },
    ]

    question = "What is photosynthesis?"

    builder = PromptBuilder()
    prompt = builder.build(question, chunks)

    generator = GroqGenerator()
    answer = generator.generate(prompt)

    assert answer is not None
    assert isinstance(answer, str)
    assert len(answer.strip()) > 0