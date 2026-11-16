from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import os

# -----------------------------
# Step 1: Load PDF
# -----------------------------
pdf_path = "C:/Users/nagan/OneDrive/Desktop/RAG/data/Reading_Material_-_Quantum_Fundamentals_ItAB6Hf-1.pdf"

if not os.path.exists(pdf_path):
    raise FileNotFoundError(f"PDF not found: {pdf_path}")

loader = PyPDFLoader(pdf_path)
documents = loader.load()

print(f"Loaded {len(documents)} pages.")

# -----------------------------
# Step 2: Split into chunks
# -----------------------------
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = text_splitter.split_documents(documents)

print(f"Created {len(chunks)} chunks.")

# -----------------------------
# Step 3: Create Embedding Model
# -----------------------------
embedding_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

print("Embedding model loaded.")

# -----------------------------
# Step 4: Create Chroma Vector DB
# -----------------------------
db = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="chroma_db"
)

print("Vector database created.")

print("✅ RAG ingestion completed successfully!")