# App/retriever.py
import os
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
    
def process_query_and_retrieve(query: str, collection_name: str, top_k: int = 3):
    """
    Takes query text, generates its embedding, and retrieves top_k matching chunks from ChromaDB.
    """
    persist_directory = os.path.join("vector_db", "chroma_db")

    # Initialize embedding model
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Load the ChromaDB collection
    print(f"📂 [INFO] Loading ChromaDB collection: {collection_name}")
    vectorstore = Chroma(
        collection_name=collection_name,
        persist_directory=persist_directory,
        embedding_function=embedding_model
    )

    # Perform similarity search
    print(f"🔎 [INFO] Performing similarity search for query: {query}")
    docs = vectorstore.similarity_search(query, k=top_k)

    # Return top matching chunks
    return [doc.page_content for doc in docs]




