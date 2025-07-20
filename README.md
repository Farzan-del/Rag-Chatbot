to run the code you must make the following folder struture for which you need to copy raw file and paste in notepad first. It will make you clear with the folder structure. Make folder structure like that and download all the libraries from requirements.txt file and then run this project.



RAG_Project/ │ ├── requirements.txt # Python dependencies ├── README.md # Project documentation │ ├── App/ # Core backend logic │ ├── api_main.py # FastAPI main backend entry point │ ├── pdf2img.py # Convert PDF to images using PyMuPDF │ ├── ocr_tesseract.py # Perform OCR on images using Tesseract │ ├── base64_utils.py # Encode/decode PDFs as Base64 │ ├── chunker.py # Chunk extracted text │ ├── embed_store.py # Generate embeddings & store in ChromaDB │ ├── retriever.py # Retrieve top-k chunks for query │ ├── llm_generator.py # Generate answers using Google Gemini API │ ├── web_search.py # Web search fallback │ ├── text_to_speech.py # Convert text answer to MP3 │ ├── streamlit_app/ # Frontend │ ├── app.py # Streamlit app for UI │ ├── Data/ # Data storage folder │ ├── Input_pdf_folder/ # Uploaded PDFs │ ├── Extracted_texts/ # Extracted text files │ ├── Chunks/ # Chunked text files │ ├── Images/ # Converted PDF pages as images │ ├── Audio/ # Generated speech MP3 files │ ├── vector_db/ # Vector Database for RAG │ ├── chroma_db/ # ChromaDB storage for embeddings │ └── .venv/ # Virtual environment (optional)

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

Requirements
See the requirements.txt file and run:
pip install -r requirements.txt

Project Workflow
Upload PDF
→ Save & decode PDF → Convert PDF pages into images.

Text Extraction
→ Apply Tesseract OCR to extract text.

Chunking & Embedding
→ Split text into chunks → Create embeddings → Store in ChromaDB.

Query Processing
→ User asks question → Retrieve top chunks using semantic search.

Answer Generation
→ Generate response using Google Gemini API.

Fallback (Optional)
→ If PDF answer not found → Search the web → Regenerate answer.

Voice Output
→ Convert response to speech (MP3) using gTTS → Stream audio in UI.

to run the code you must make the following folder struture
RAG_Project/
│
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
│
├── App/                         # Core backend logic
│   ├── api_main.py              # FastAPI main backend entry point
│   ├── pdf2img.py               # Convert PDF to images using PyMuPDF
│   ├── ocr_tesseract.py         # Perform OCR on images using Tesseract
│   ├── base64_utils.py          # Encode/decode PDFs as Base64
│   ├── chunker.py               # Chunk extracted text
│   ├── embed_store.py           # Generate embeddings & store in ChromaDB
│   ├── retriever.py             # Retrieve top-k chunks for query
│   ├── llm_generator.py         # Generate answers using Google Gemini API
│   ├── web_search.py            # Web search fallback
│   ├── text_to_speech.py        # Convert text answer to MP3
│
├── streamlit_app/               # Frontend
│   ├── app.py                   # Streamlit app for UI
│
├── Data/                        # Data storage folder
│   ├── Input_pdf_folder/        # Uploaded PDFs
│   ├── Extracted_texts/         # Extracted text files
│   ├── Chunks/                  # Chunked text files
│   ├── Images/                  # Converted PDF pages as images
│   ├── Audio/                   # Generated speech MP3 files
│
├── vector_db/                   # Vector Database for RAG
│   ├── chroma_db/               # ChromaDB storage for embeddings
│
└── .venv/                       # Virtual environment (optional)
