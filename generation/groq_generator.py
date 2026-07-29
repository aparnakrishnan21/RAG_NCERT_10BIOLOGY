import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()


class GroqGenerator:

    def __init__(self, model="llama-3.3-70b-versatile"):

        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError("GROQ_API_KEY not found in .env file.")

        self.client = Groq(api_key=api_key)
        self.model = model

    def generate(self, prompt):

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0,
            max_tokens=512,
        )

        return response.choices[0].message.content.strip()