# App/embed_store.py
import os
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

def create_embeddings_and_store(chunk_file: str, collection_name: str = "pdf_chunks"):
    """
    Reads text chunks, creates embeddings, and stores them in ChromaDB.
    """
    if not os.path.exists(chunk_file):
        raise FileNotFoundError(f"Chunk file not found: {chunk_file}")

    # Read chunks from file
    with open(chunk_file, "r", encoding="utf-8") as f:
        chunks = [chunk.strip() for chunk in f.read().split("---CHUNK---") if chunk.strip()]

    # Initialize embeddings model
    print(" [INFO] Loading embedding model...")
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Define ChromaDB persistent directory
    persist_directory = os.path.join("vector_db", "chroma_db")
    os.makedirs(persist_directory, exist_ok=True)

    # Create ChromaDB collection and store embeddings
    print(f" [INFO] Creating ChromaDB collection: {collection_name}")
    vectorstore = Chroma.from_texts(texts=chunks, embedding=embedding_model, collection_name=collection_name, persist_directory=persist_directory)

    # Persist data
    vectorstore.persist()
    print(f" [INFO] Stored {len(chunks)} chunks in ChromaDB at {persist_directory}")

    return {
        "collection_name": collection_name,
        "chunks_stored": len(chunks),
        "persist_directory": persist_directory
    }
