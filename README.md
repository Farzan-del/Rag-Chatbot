📚 RAG-Powered Chatbot with Voice
This project is an AI-powered Retrieval-Augmented Generation (RAG) chatbot that enables users to upload PDFs, extract text, and query the content intelligently. It leverages OCR for scanned PDFs, vector embeddings for document search, and an advanced LLM (Google Gemini) for generating precise, context-aware answers. If the relevant answer is not found in the uploaded document, the system optionally performs a web search to enrich responses, ensuring maximum accuracy.

Key features include:
✔ PDF Upload & Processing – Converts PDFs into images using PyMuPDF, extracts text with Tesseract OCR, and stores it in a structured format.
✔ Text Chunking & Vector Storage – Splits extracted text into manageable chunks and stores embeddings in ChromaDB for efficient semantic search.
✔ Contextual Query Handling – Answers questions by retrieving relevant text from the document; falls back to web search only if necessary.
✔ Generative AI Response – Uses Google Gemini API to generate human-like answers based on retrieved document context.
✔ Voice Integration – Converts answers into speech using gTTS, providing an audio playback option directly in the Streamlit UI.
✔ Interactive Frontend – Built with Streamlit, featuring an intuitive PDF upload sidebar, real-time Q&A chat interface, and embedded audio controls for listening to responses.

This solution is designed for students, researchers, and professionals who need an efficient way to extract knowledge from documents and interact with them conversationally. It blends information retrieval, generative AI, and speech synthesis to create a powerful, user-friendly tool for document-based Q&A.

Tech Stack:

Backend: FastAPI, PyMuPDF, Tesseract OCR, ChromaDB, Sentence Transformers
AI Model: Google Gemini API
Frontend: Streamlit
Voice: gTTS for Text-to-Speech
Other Tools: Requests, Uvicorn, Web Search APIs
