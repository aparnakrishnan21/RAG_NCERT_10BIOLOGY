import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/ask"

st.set_page_config(
    page_title="Hybrid RAG",
    page_icon="📚",
    layout="wide"
)

st.title("📚 NCERT Biology Hybrid RAG")
st.write("Ask questions from the NCERT Biology textbook.")

question = st.text_input(
    "Enter your question:"
)

if st.button("Ask"):

    if question.strip():

        with st.spinner("Searching..."):

            response = requests.post(
                API_URL,
                json={
                    "question": question
                }
            )

            if response.status_code == 200:

                answer = response.json()["answer"]

                st.success("Answer")

                st.write(answer)

            else:

                st.error("Error communicating with API.")