import streamlit as st

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaLLM

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(page_title="RAG Chatbot", page_icon="🤖")

st.title("🤖 PDF RAG Chatbot")
st.write("Ask questions from your PDF.")

# -------------------------
# Load Embedding Model
# -------------------------
embedding_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

# -------------------------
# Load Chroma Database
# -------------------------
db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding_model
)

retriever = db.as_retriever(search_kwargs={"k": 3})

# -------------------------
# Load Ollama Model
# -------------------------
llm = OllamaLLM(model="gemma3")

# -------------------------
# User Input
# -------------------------
question = st.text_input("Enter your question:")

if st.button("Ask"):

    if question.strip() == "":
        st.warning("Please enter a question.")
    else:

        docs = retriever.invoke(question)

        context = "\n\n".join([doc.page_content for doc in docs])

        prompt = f"""
You are a helpful assistant.

Answer ONLY from the context below.

Context:
{context}

Question:
{question}

Answer:
"""

        answer = llm.invoke(prompt)

        st.subheader("Answer")
        st.write(answer)

        with st.expander("Retrieved Context"):
            st.write(context)
