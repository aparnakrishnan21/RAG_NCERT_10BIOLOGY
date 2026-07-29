from fastapi import FastAPI
from app.schemas import QuestionRequest, AnswerResponse
from app.rag_pipeline import ask_question

app = FastAPI(
    title="Hybrid RAG API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Hybrid RAG API is running!"
    }


@app.post("/ask", response_model=AnswerResponse)
def ask(request: QuestionRequest):

    answer = ask_question(request.question)

    return AnswerResponse(answer=answer)