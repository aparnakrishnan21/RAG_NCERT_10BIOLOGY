from generation.groq_generator import GroqGenerator

generator = GroqGenerator()

prompt = """
Explain photosynthesis in two sentences.
"""

answer = generator.generate(prompt)

print("\nAnswer:\n")
print(answer)