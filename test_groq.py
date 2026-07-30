# 
from generation.groq_generator import GroqGenerator

def test_groq_generation():
    generator = GroqGenerator()

    prompt = "Explain photosynthesis in two sentences."

    answer = generator.generate(prompt)

    assert answer is not None
    assert isinstance(answer, str)
    assert len(answer.strip()) > 0