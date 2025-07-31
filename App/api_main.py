

# from fastapi import FastAPI, File, UploadFile
# import shutil
# import os

# from App.pdf2img import convert_pdf_to_image
# from App.ocr_tesseract import run_ocr_on_images
# from App.base64_utils import encode_pdf_to_base64, decode_base64_to_pdf
# from App.chunker import chunk_text_file
# from App.embed_store import create_embeddings_and_store

# app = FastAPI()

# # === Directories ===
# UPLOAD_DIR = os.path.join("Data", "Input_pdf_folder")
# TEXT_OUTPUT_DIR = os.path.join("Data", "Extracted_texts")
# CHUNK_DIR = os.path.join("Data", "Chunks")

# # Ensure directories exist
# os.makedirs(UPLOAD_DIR, exist_ok=True)
# os.makedirs(TEXT_OUTPUT_DIR, exist_ok=True)
# os.makedirs(CHUNK_DIR, exist_ok=True)


# @app.post("/upload/")
# async def upload_file(file: UploadFile = File(...)):
#     print("✅ [INFO] Upload API called")

#     # === Step 1: Save uploaded PDF ===
#     pdf_filename = file.filename
#     original_pdf_path = os.path.join(UPLOAD_DIR, pdf_filename)
#     print(f"📂 [INFO] Saving uploaded file to: {original_pdf_path}")
#     with open(original_pdf_path, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)
#     print("✅ [INFO] Original PDF saved successfully!")

#     # === Step 2: Encode PDF to Base64 ===
#     print("🔄 [INFO] Encoding PDF to Base64...")
#     pdf_base64 = encode_pdf_to_base64(original_pdf_path)
#     print("✅ [INFO] PDF encoded to Base64.")

#     # === Step 3: Decode Base64 back to PDF ===
#     decoded_pdf_path = os.path.join(UPLOAD_DIR, f"decoded_{pdf_filename}")
#     print(f"🔄 [INFO] Decoding Base64 back to PDF: {decoded_pdf_path}")
#     decode_base64_to_pdf(pdf_base64, decoded_pdf_path)
#     print("✅ [INFO] PDF decoded successfully!")

#     # === Step 4: Prepare output text file path ===
#     base_filename = os.path.splitext(pdf_filename)[0]
#     output_text_path = os.path.join(TEXT_OUTPUT_DIR, f"{base_filename}.txt")
#     print(f"📝 [INFO] Output text will be saved at: {output_text_path}")

#     # === Step 5: Convert decoded PDF to Images ===
#     print("🔄 [INFO] Converting decoded PDF to images...")
#     image_paths = convert_pdf_to_image(f"decoded_{pdf_filename}")
#     print(f"✅ [INFO] Decoded PDF converted into {len(image_paths)} image(s): {image_paths}")

#     # === Step 6: Run OCR on Images ===
#     print("🔍 [INFO] Running OCR on images...")
#     run_ocr_on_images(image_paths, output_text_path)
#     print(f"✅ [INFO] OCR complete. Extracted text saved to: {output_text_path}")

#     # === Step 7: Chunk text into character-based chunks ===
#     chunk_output_path = os.path.join(CHUNK_DIR, f"{base_filename}_chunks.txt")
#     print(f"🔄 [INFO] Chunking text into chunks...")
#     num_chunks = chunk_text_file(output_text_path, chunk_output_path, chunk_size=1000)
#     print(f"✅ [INFO] Created {num_chunks} chunks in {chunk_output_path}")

#     # === Step 8: Create embeddings and store in ChromaDB ===
#     print("🔄 [INFO] Creating embeddings and storing in ChromaDB...")
#     embedding_result = create_embeddings_and_store(chunk_output_path, collection_name=base_filename)
#     print(f"✅ [INFO] Embeddings stored for {embedding_result['chunks_stored']} chunks")

#     return {
#         "message": "PDF processed, text extracted, chunked, and embeddings stored successfully",
#         "original_pdf": original_pdf_path,
#         "decoded_pdf": decoded_pdf_path,
#         "text_file": output_text_path,
#         "chunks_file": chunk_output_path,
#         "num_chunks": num_chunks,
#         "embeddings_info": embedding_result,
#         "total_pages": len(image_paths),
#         "base64_preview": pdf_base64[:50] + "..."  # For debugging
#     }


# from fastapi import FastAPI, File, UploadFile, Form
# import shutil
# import os

# from App.pdf2img import convert_pdf_to_image
# from App.ocr_tesseract import run_ocr_on_images
# from App.base64_utils import encode_pdf_to_base64, decode_base64_to_pdf
# from App.chunker import chunk_text_file
# from App.embed_store import create_embeddings_and_store
# from App.retriever import process_query_and_retrieve

# app = FastAPI()

# # === Directories ===
# UPLOAD_DIR = os.path.join("Data", "Input_pdf_folder")
# TEXT_OUTPUT_DIR = os.path.join("Data", "Extracted_texts")
# CHUNK_DIR = os.path.join("Data", "Chunks")

# # Ensure directories exist
# os.makedirs(UPLOAD_DIR, exist_ok=True)
# os.makedirs(TEXT_OUTPUT_DIR, exist_ok=True)
# os.makedirs(CHUNK_DIR, exist_ok=True)


# @app.post("/upload/")
# async def upload_file(file: UploadFile = File(...)):
#     print("✅ [INFO] Upload API called")

#     # === Step 1: Save uploaded PDF ===
#     pdf_filename = file.filename
#     original_pdf_path = os.path.join(UPLOAD_DIR, pdf_filename)
#     print(f"📂 [INFO] Saving uploaded file to: {original_pdf_path}")
#     with open(original_pdf_path, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)
#     print("✅ [INFO] Original PDF saved successfully!")

#     # === Step 2: Encode PDF to Base64 ===
#     print("🔄 [INFO] Encoding PDF to Base64...")
#     pdf_base64 = encode_pdf_to_base64(original_pdf_path)
#     print("✅ [INFO] PDF encoded to Base64.")

#     # === Step 3: Decode Base64 back to PDF ===
#     decoded_pdf_path = os.path.join(UPLOAD_DIR, f"decoded_{pdf_filename}")
#     print(f"🔄 [INFO] Decoding Base64 back to PDF: {decoded_pdf_path}")
#     decode_base64_to_pdf(pdf_base64, decoded_pdf_path)
#     print("✅ [INFO] PDF decoded successfully!")

#     # === Step 4: Prepare output text file path ===
#     base_filename = os.path.splitext(pdf_filename)[0]
#     output_text_path = os.path.join(TEXT_OUTPUT_DIR, f"{base_filename}.txt")
#     print(f"📝 [INFO] Output text will be saved at: {output_text_path}")

#     # === Step 5: Convert decoded PDF to Images ===
#     print("🔄 [INFO] Converting decoded PDF to images...")
#     image_paths = convert_pdf_to_image(f"decoded_{pdf_filename}")
#     print(f"✅ [INFO] Decoded PDF converted into {len(image_paths)} image(s): {image_paths}")

#     # === Step 6: Run OCR on Images ===
#     print("🔍 [INFO] Running OCR on images...")
#     run_ocr_on_images(image_paths, output_text_path)
#     print(f"✅ [INFO] OCR complete. Extracted text saved to: {output_text_path}")

#     # === Step 7: Chunk text into character-based chunks ===
#     chunk_output_path = os.path.join(CHUNK_DIR, f"{base_filename}_chunks.txt")
#     print(f"🔄 [INFO] Chunking text into chunks...")
#     num_chunks = chunk_text_file(output_text_path, chunk_output_path, chunk_size=1000)
#     print(f"✅ [INFO] Created {num_chunks} chunks in {chunk_output_path}")

#     # === Step 8: Create embeddings and store in ChromaDB ===
#     print("🔄 [INFO] Creating embeddings and storing in ChromaDB...")
#     embedding_result = create_embeddings_and_store(chunk_output_path, collection_name=base_filename)
#     print(f"✅ [INFO] Embeddings stored for {embedding_result['chunks_stored']} chunks")

#     return {
#         "message": "PDF processed, text extracted, chunked, and embeddings stored successfully",
#         "original_pdf": original_pdf_path,
#         "decoded_pdf": decoded_pdf_path,
#         "text_file": output_text_path,
#         "chunks_file": chunk_output_path,
#         "num_chunks": num_chunks,
#         "embeddings_info": embedding_result,
#         "total_pages": len(image_paths),
#         "base64_preview": pdf_base64[:50] + "..."  # For debugging
#     }


# @app.post("/query/")
# async def query_document(query: str = Form(...), collection_name: str = Form(...)):
#     """
#     Takes user query, chunks it, creates embeddings, and retrieves relevant results from ChromaDB.
#     """
#     print(f"🔍 [INFO] Query received: {query}")
#     results = process_query_and_retrieve(query, collection_name=collection_name, top_k=3)

#     return {
#         "query": query,
#         "top_results": results
#     }



# from fastapi import FastAPI, File, UploadFile, Form
# import shutil
# import os

# from App.pdf2img import convert_pdf_to_image
# from App.ocr_tesseract import run_ocr_on_images
# from App.base64_utils import encode_pdf_to_base64, decode_base64_to_pdf
# from App.chunker import chunk_text_file
# from App.embed_store import create_embeddings_and_store
# from App.retriever import process_query_and_retrieve
# from App.llm_generator import generate_answer_with_gemini

# app = FastAPI()

# # === Directories ===
# UPLOAD_DIR = os.path.join("Data", "Input_pdf_folder")
# TEXT_OUTPUT_DIR = os.path.join("Data", "Extracted_texts")
# CHUNK_DIR = os.path.join("Data", "Chunks")

# # Ensure directories exist
# os.makedirs(UPLOAD_DIR, exist_ok=True)
# os.makedirs(TEXT_OUTPUT_DIR, exist_ok=True)
# os.makedirs(CHUNK_DIR, exist_ok=True)


# @app.post("/upload/")
# async def upload_file(file: UploadFile = File(...)):
#     print("✅ [INFO] Upload API called")

#     # === Step 1: Save uploaded PDF ===
#     pdf_filename = file.filename
#     original_pdf_path = os.path.join(UPLOAD_DIR, pdf_filename)
#     with open(original_pdf_path, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)
#     print("✅ [INFO] Original PDF saved successfully!")

#     # === Step 2: Encode PDF to Base64 ===
#     pdf_base64 = encode_pdf_to_base64(original_pdf_path)
#     print("✅ [INFO] PDF encoded to Base64.")

#     # === Step 3: Decode Base64 back to PDF ===
#     decoded_pdf_path = os.path.join(UPLOAD_DIR, f"decoded_{pdf_filename}")
#     decode_base64_to_pdf(pdf_base64, decoded_pdf_path)
#     print("✅ [INFO] PDF decoded successfully!")

#     # === Step 4: Prepare output text file path ===
#     base_filename = os.path.splitext(pdf_filename)[0]
#     output_text_path = os.path.join(TEXT_OUTPUT_DIR, f"{base_filename}.txt")

#     # === Step 5: Convert decoded PDF to Images ===
#     image_paths = convert_pdf_to_image(f"decoded_{pdf_filename}")
#     print(f"✅ [INFO] Decoded PDF converted into {len(image_paths)} image(s).")

#     # === Step 6: Run OCR on Images ===
#     run_ocr_on_images(image_paths, output_text_path)
#     print(f"✅ [INFO] OCR complete. Extracted text saved to: {output_text_path}")

#     # === Step 7: Chunk text ===
#     chunk_output_path = os.path.join(CHUNK_DIR, f"{base_filename}_chunks.txt")
#     num_chunks = chunk_text_file(output_text_path, chunk_output_path, chunk_size=1000)
#     print(f"✅ [INFO] Created {num_chunks} chunks.")

#     # === Step 8: Create embeddings and store in ChromaDB ===
#     embedding_result = create_embeddings_and_store(chunk_output_path, collection_name=base_filename)
#     print(f"✅ [INFO] Embeddings stored for {embedding_result['chunks_stored']} chunks")

#     return {
#         "message": "PDF processed and embeddings stored successfully",
#         "original_pdf": original_pdf_path,
#         "decoded_pdf": decoded_pdf_path,
#         "text_file": output_text_path,
#         "chunks_file": chunk_output_path,
#         "num_chunks": num_chunks,
#         "embeddings_info": embedding_result,
#         "total_pages": len(image_paths),
#         "base64_preview": pdf_base64[:50] + "..."
#     }


# @app.post("/query/")
# async def query_document(query: str = Form(...), collection_name: str = Form(...)):
#     """
#     Takes user query, retrieves top relevant chunks from ChromaDB, and generates an answer using Gemini.
#     """
#     print(f"🔍 [INFO] Query received: {query}")

#     # Step 1: Retrieve relevant chunks
#     retrieved_chunks = process_query_and_retrieve(query, collection_name=collection_name, top_k=3)

#     # Step 2: Generate answer using Gemini
#     answer = generate_answer_with_gemini(query, retrieved_chunks)
    
#     return {
#         "query": query,
#         "retrieved_chunks": retrieved_chunks,
#         "answer": answer
#     }




# from fastapi import FastAPI, File, UploadFile, Form
# import shutil
# import os

# from App.pdf2img import convert_pdf_to_image
# from App.ocr_tesseract import run_ocr_on_images
# from App.base64_utils import encode_pdf_to_base64, decode_base64_to_pdf
# from App.chunker import chunk_text_file
# from App.embed_store import create_embeddings_and_store
# from App.retriever import process_query_and_retrieve
# from App.llm_generator import generate_answer_with_gemini
# from App.web_search import get_web_search_results

# app = FastAPI()

# # === Directories ===
# UPLOAD_DIR = os.path.join("Data", "Input_pdf_folder")
# TEXT_OUTPUT_DIR = os.path.join("Data", "Extracted_texts")
# CHUNK_DIR = os.path.join("Data", "Chunks")

# # Ensure directories exist
# os.makedirs(UPLOAD_DIR, exist_ok=True)
# os.makedirs(TEXT_OUTPUT_DIR, exist_ok=True)
# os.makedirs(CHUNK_DIR, exist_ok=True)


# @app.post("/upload/")
# async def upload_file(file: UploadFile = File(...)):
#     print("✅ [INFO] Upload API called")

#     # === Step 1: Save uploaded PDF ===
#     pdf_filename = file.filename
#     original_pdf_path = os.path.join(UPLOAD_DIR, pdf_filename)
#     with open(original_pdf_path, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)
#     print("✅ [INFO] Original PDF saved successfully!")

#     # === Step 2: Encode PDF to Base64 ===
#     pdf_base64 = encode_pdf_to_base64(original_pdf_path)
#     print("✅ [INFO] PDF encoded to Base64.")

#     # === Step 3: Decode Base64 back to PDF ===
#     decoded_pdf_path = os.path.join(UPLOAD_DIR, f"decoded_{pdf_filename}")
#     decode_base64_to_pdf(pdf_base64, decoded_pdf_path)
#     print("✅ [INFO] PDF decoded successfully!")

#     # === Step 4: Prepare output text file path ===
#     base_filename = os.path.splitext(pdf_filename)[0]
#     output_text_path = os.path.join(TEXT_OUTPUT_DIR, f"{base_filename}.txt")

#     # === Step 5: Convert decoded PDF to Images ===
#     image_paths = convert_pdf_to_image(f"decoded_{pdf_filename}")
#     print(f"✅ [INFO] Decoded PDF converted into {len(image_paths)} image(s).")

#     # === Step 6: Run OCR on Images ===
#     run_ocr_on_images(image_paths, output_text_path)
#     print(f"✅ [INFO] OCR complete. Extracted text saved to: {output_text_path}")

#     # === Step 7: Chunk text ===
#     chunk_output_path = os.path.join(CHUNK_DIR, f"{base_filename}_chunks.txt")
#     num_chunks = chunk_text_file(output_text_path, chunk_output_path, chunk_size=1000)
#     print(f"✅ [INFO] Created {num_chunks} chunks.")

#     # === Step 8: Create embeddings and store in ChromaDB ===
#     embedding_result = create_embeddings_and_store(chunk_output_path, collection_name=base_filename)
#     print(f"✅ [INFO] Embeddings stored for {embedding_result['chunks_stored']} chunks")

#     return {
#         "message": "PDF processed and embeddings stored successfully",
#         "original_pdf": original_pdf_path,
#         "decoded_pdf": decoded_pdf_path,
#         "text_file": output_text_path,
#         "chunks_file": chunk_output_path,
#         "num_chunks": num_chunks,
#         "embeddings_info": embedding_result,
#         "total_pages": len(image_paths),
#         "base64_preview": pdf_base64[:50] + "..."
#     }


# @app.post("/query/")
# async def query_document(query: str = Form(...), collection_name: str = Form(...)):
#     """
#     Tries to answer from the PDF (RAG). If not found, fetch from web.
#     """
#     print(f"🔍 [INFO] Query received: {query}")

#     # Step 1: Retrieve relevant chunks
#     retrieved_chunks = process_query_and_retrieve(query, collection_name=collection_name, top_k=3)

#     # Step 2: Try generating answer using Gemini with PDF context
#     answer = generate_answer_with_gemini(query, retrieved_chunks)

#     # Step 3: If answer is empty or says 'not available', try web search
#     if "Based on the provided document, the answer is not available." in answer or not answer.strip():
#         print("[INFO] Answer not found in PDF. Searching the web...")
#         web_results = get_web_search_results(query)
#         answer = generate_answer_with_gemini(query, web_results)  # Use web content as context

#     return {
#         "query": query,
#         "retrieved_chunks": retrieved_chunks,
#         "answer": answer
#     }




# from fastapi import FastAPI, File, UploadFile, Form
# import shutil
# import os

# from App.pdf2img import convert_pdf_to_image
# from App.ocr_tesseract import run_ocr_on_images
# from App.base64_utils import encode_pdf_to_base64, decode_base64_to_pdf
# from App.chunker import chunk_text_file
# from App.embed_store import create_embeddings_and_store
# from App.retriever import process_query_and_retrieve
# from App.llm_generator import generate_answer_with_gemini
# from App.web_search import get_web_search_results

# app = FastAPI()

# # === Directories ===
# UPLOAD_DIR = os.path.join("Data", "Input_pdf_folder")
# TEXT_OUTPUT_DIR = os.path.join("Data", "Extracted_texts")
# CHUNK_DIR = os.path.join("Data", "Chunks")

# # Ensure directories exist
# os.makedirs(UPLOAD_DIR, exist_ok=True)
# os.makedirs(TEXT_OUTPUT_DIR, exist_ok=True)
# os.makedirs(CHUNK_DIR, exist_ok=True)


# @app.post("/upload/")
# async def upload_file(file: UploadFile = File(...)):
#     print("✅ [INFO] Upload API called")

#     # === Step 1: Save uploaded PDF ===
#     pdf_filename = file.filename
#     original_pdf_path = os.path.join(UPLOAD_DIR, pdf_filename)
#     with open(original_pdf_path, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)
#     print("✅ [INFO] Original PDF saved successfully!")

#     # === Step 2: Encode PDF to Base64 ===
#     pdf_base64 = encode_pdf_to_base64(original_pdf_path)
#     print("✅ [INFO] PDF encoded to Base64.")

#     # === Step 3: Decode Base64 back to PDF ===
#     decoded_pdf_path = os.path.join(UPLOAD_DIR, f"decoded_{pdf_filename}")
#     decode_base64_to_pdf(pdf_base64, decoded_pdf_path)
#     print("✅ [INFO] PDF decoded successfully!")

#     # === Step 4: Prepare output text file path ===
#     base_filename = os.path.splitext(pdf_filename)[0]
#     output_text_path = os.path.join(TEXT_OUTPUT_DIR, f"{base_filename}.txt")

#     # === Step 5: Convert decoded PDF to Images ===
#     image_paths = convert_pdf_to_image(f"decoded_{pdf_filename}")
#     print(f"✅ [INFO] Decoded PDF converted into {len(image_paths)} image(s).")

#     # === Step 6: Run OCR on Images ===
#     run_ocr_on_images(image_paths, output_text_path)
#     print(f"✅ [INFO] OCR complete. Extracted text saved to: {output_text_path}")

#     # === Step 7: Chunk text ===
#     chunk_output_path = os.path.join(CHUNK_DIR, f"{base_filename}_chunks.txt")
#     num_chunks = chunk_text_file(output_text_path, chunk_output_path, chunk_size=1000)
#     print(f"✅ [INFO] Created {num_chunks} chunks.")

#     # === Step 8: Create embeddings and store in ChromaDB ===
#     embedding_result = create_embeddings_and_store(chunk_output_path, collection_name=base_filename)
#     print(f"✅ [INFO] Embeddings stored for {embedding_result['chunks_stored']} chunks")

#     return {
#         "message": "PDF processed and embeddings stored successfully",
#         "original_pdf": original_pdf_path,
#         "decoded_pdf": decoded_pdf_path,
#         "text_file": output_text_path,
#         "chunks_file": chunk_output_path,
#         "num_chunks": num_chunks,
#         "embeddings_info": embedding_result,
#         "total_pages": len(image_paths),
#         "base64_preview": pdf_base64[:50] + "..."
#     }


# @app.post("/query/")
# async def query_document(query: str = Form(...), collection_name: str = Form(...)):
#     """
#     Tries to answer from the PDF (RAG). If not found, fetch from web.
#     """
#     print(f"🔍 [INFO] Query received: {query}")

#     # Step 1: Retrieve relevant chunks
#     retrieved_chunks = process_query_and_retrieve(query, collection_name=collection_name, top_k=3)

#     # Step 2: Try generating answer using Gemini with PDF context
#     answer = generate_answer_with_gemini(query, retrieved_chunks)

#     # Step 3: If answer is empty or says 'not available', try web search
#     if "Based on the provided document, the answer is not available." in answer or not answer.strip():
#         print("[INFO] Answer not found in PDF. Searching the web...")
#         web_results = get_web_search_results(query)
#         answer = generate_answer_with_gemini(query, web_results)  # Use web content as context

#     return {
#         "query": query,
#         "retrieved_chunks": retrieved_chunks,
#         "answer": answer
#     }

# from fastapi import FastAPI, File, UploadFile, Form
# import shutil
# import os

# from App.pdf2img import convert_pdf_to_image
# from App.ocr_tesseract import run_ocr_on_images
# from App.base64_utils import encode_pdf_to_base64, decode_base64_to_pdf
# from App.chunker import chunk_text_file
# from App.embed_store import create_embeddings_and_store
# from App.retriever import process_query_and_retrieve
# from App.llm_generator import generate_answer_with_gemini
# from App.web_search import get_web_search_results
# from App.text_to_speech import convert_text_to_speech

# app = FastAPI()

# # === Directories ===
# UPLOAD_DIR = os.path.join("Data", "Input_pdf_folder")
# TEXT_OUTPUT_DIR = os.path.join("Data", "Extracted_texts")
# CHUNK_DIR = os.path.join("Data", "Chunks")

# # Ensure directories exist
# os.makedirs(UPLOAD_DIR, exist_ok=True)
# os.makedirs(TEXT_OUTPUT_DIR, exist_ok=True)
# os.makedirs(CHUNK_DIR, exist_ok=True)


# @app.post("/upload/")
# async def upload_file(file: UploadFile = File(...)):
#     print("✅ [INFO] Upload API called")

#     # === Step 1: Save uploaded PDF ===
#     pdf_filename = file.filename
#     original_pdf_path = os.path.join(UPLOAD_DIR, pdf_filename)
#     with open(original_pdf_path, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)
#     print("✅ [INFO] Original PDF saved successfully!")

#     # === Step 2: Encode PDF to Base64 ===
#     pdf_base64 = encode_pdf_to_base64(original_pdf_path)
#     print("✅ [INFO] PDF encoded to Base64.")

#     # === Step 3: Decode Base64 back to PDF ===
#     decoded_pdf_path = os.path.join(UPLOAD_DIR, f"decoded_{pdf_filename}")
#     decode_base64_to_pdf(pdf_base64, decoded_pdf_path)
#     print("✅ [INFO] PDF decoded successfully!")

#     # === Step 4: Prepare output text file path ===
#     base_filename = os.path.splitext(pdf_filename)[0]
#     output_text_path = os.path.join(TEXT_OUTPUT_DIR, f"{base_filename}.txt")

#     # === Step 5: Convert decoded PDF to Images ===
#     image_paths = convert_pdf_to_image(f"decoded_{pdf_filename}")
#     print(f"✅ [INFO] Decoded PDF converted into {len(image_paths)} image(s).")

#     # === Step 6: Run OCR on Images ===
#     run_ocr_on_images(image_paths, output_text_path)
#     print(f"✅ [INFO] OCR complete. Extracted text saved to: {output_text_path}")

#     # === Step 7: Chunk text ===
#     chunk_output_path = os.path.join(CHUNK_DIR, f"{base_filename}_chunks.txt")
#     num_chunks = chunk_text_file(output_text_path, chunk_output_path, chunk_size=1000)
#     print(f"✅ [INFO] Created {num_chunks} chunks.")

#     # === Step 8: Create embeddings and store in ChromaDB ===
#     embedding_result = create_embeddings_and_store(chunk_output_path, collection_name=base_filename)
#     print(f"✅ [INFO] Embeddings stored for {embedding_result['chunks_stored']} chunks")

#     return {
#         "message": "PDF processed and embeddings stored successfully",
#         "original_pdf": original_pdf_path,
#         "decoded_pdf": decoded_pdf_path,
#         "text_file": output_text_path,
#         "chunks_file": chunk_output_path,
#         "num_chunks": num_chunks,
#         "embeddings_info": embedding_result,
#         "total_pages": len(image_paths),
#         "base64_preview": pdf_base64[:50] + "..."
#     }


# @app.post("/query/")
# async def query_document(query: str = Form(...), collection_name: str = Form(...)):
#     """
#     Tries to answer from the PDF (RAG). If not found, fetch from web.
#     """
#     print(f"🔍 [INFO] Query received: {query}")

#     # Step 1: Retrieve relevant chunks
#     retrieved_chunks = process_query_and_retrieve(query, collection_name=collection_name, top_k=3)

#     # Step 2: Try generating answer using Gemini with PDF context
#     answer = generate_answer_with_gemini(query, retrieved_chunks)

#     # Step 3: If answer is empty or says 'not available', try web search
#     if "Based on the provided document, the answer is not available." in answer or not answer.strip():
#         print("[INFO] Answer not found in PDF. Searching the web...")
#         web_results = get_web_search_results(query)
#         answer = generate_answer_with_gemini(query, web_results)  # Use web content as context

#     audio_path = convert_text_to_speech(answer)

#     return {
#         "query": query,
#         "retrieved_chunks": retrieved_chunks,
#         "answer": answer,
#         "audio_file": audio_path
#     }


# from fastapi import FastAPI, File, UploadFile, Form
# from fastapi.responses import FileResponse


# import shutil
# import os

# from App.pdf2img import convert_pdf_to_image
# from App.ocr_tesseract import run_ocr_on_images
# from App.base64_utils import encode_pdf_to_base64, decode_base64_to_pdf
# from App.chunker import chunk_text_file
# from App.embed_store import create_embeddings_and_store
# from App.retriever import process_query_and_retrieve
# from App.llm_generator import generate_answer_with_gemini
# from App.web_search import get_web_search_results
# from App.text_to_speech import convert_text_to_speech

# app = FastAPI()

# # === Directories ===
# UPLOAD_DIR = os.path.join("Data", "Input_pdf_folder")
# TEXT_OUTPUT_DIR = os.path.join("Data", "Extracted_texts")
# CHUNK_DIR = os.path.join("Data", "Chunks")
# AUDIO_DIR = os.path.join("Data", "Audio")

# # Ensure directories exist
# os.makedirs(UPLOAD_DIR, exist_ok=True)
# os.makedirs(TEXT_OUTPUT_DIR, exist_ok=True)
# os.makedirs(CHUNK_DIR, exist_ok=True)
# os.makedirs(AUDIO_DIR, exist_ok=True)




# @app.post("/upload/")
# async def upload_file(file: UploadFile = File(...)):
#     print("✅ [INFO] Upload API called")

#     # === Step 1: Save uploaded PDF ===
#     pdf_filename = file.filename
#     original_pdf_path = os.path.join(UPLOAD_DIR, pdf_filename)
#     with open(original_pdf_path, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)
#     print("✅ [INFO] Original PDF saved successfully!")

#     # === Step 2: Encode PDF to Base64 ===
#     pdf_base64 = encode_pdf_to_base64(original_pdf_path)
#     print("✅ [INFO] PDF encoded to Base64.")

#     # === Step 3: Decode Base64 back to PDF ===
#     decoded_pdf_path = os.path.join(UPLOAD_DIR, f"decoded_{pdf_filename}")
#     decode_base64_to_pdf(pdf_base64, decoded_pdf_path)
#     print("✅ [INFO] PDF decoded successfully!")

#     # === Step 4: Prepare output text file path ===
#     base_filename = os.path.splitext(pdf_filename)[0]
#     output_text_path = os.path.join(TEXT_OUTPUT_DIR, f"{base_filename}.txt")

#     # === Step 5: Convert decoded PDF to Images ===
#     image_paths = convert_pdf_to_image(f"decoded_{pdf_filename}")
#     print(f"✅ [INFO] Decoded PDF converted into {len(image_paths)} image(s).")

#     # === Step 6: Run OCR on Images ===
#     run_ocr_on_images(image_paths, output_text_path)
#     print(f"✅ [INFO] OCR complete. Extracted text saved to: {output_text_path}")

#     # === Step 7: Chunk text ===
#     chunk_output_path = os.path.join(CHUNK_DIR, f"{base_filename}_chunks.txt")
#     num_chunks = chunk_text_file(output_text_path, chunk_output_path, chunk_size=1000)
#     print(f"✅ [INFO] Created {num_chunks} chunks.")

#     # === Step 8: Create embeddings and store in ChromaDB ===
#     embedding_result = create_embeddings_and_store(chunk_output_path, collection_name=base_filename)
#     print(f"✅ [INFO] Embeddings stored for {embedding_result['chunks_stored']} chunks")

#     return {
#         "message": "PDF processed and embeddings stored successfully",
#         "original_pdf": original_pdf_path,
#         "decoded_pdf": decoded_pdf_path,
#         "text_file": output_text_path,
#         "chunks_file": chunk_output_path,
#         "num_chunks": num_chunks,
#         "embeddings_info": embedding_result,
#         "total_pages": len(image_paths),
#         "base64_preview": pdf_base64[:50] + "..."
#     }


# @app.post("/query/")
# async def query_document(query: str = Form(...), collection_name: str = Form(...)):
#     """
#     Tries to answer from the PDF (RAG). If not found, fetch from web.
#     Also generates speech for the answer.
#     """
#     print(f"🔍 [INFO] Query received: {query}")

#     # Step 1: Retrieve relevant chunks
#     retrieved_chunks = process_query_and_retrieve(query, collection_name=collection_name, top_k=3)

#     # Step 2: Try generating answer using Gemini with PDF context
#     answer = generate_answer_with_gemini(query, retrieved_chunks)

#     # Step 3: If answer is empty or says 'not available', try web search
#     if "Based on the provided document, the answer is not available." in answer or not answer.strip():
#         print("[INFO] Answer not found in PDF. Searching the web...")
#         web_results = get_web_search_results(query)
#         answer = generate_answer_with_gemini(query, web_results)

#     # Step 4: Convert text to speech and save in AUDIO_DIR
#     audio_path = convert_text_to_speech(answer)
#     audio_url = f"http://localhost:8000/get-audio/{os.path.basename(audio_path)}"

#     return {
#     "query": query,
#     "retrieved_chunks": retrieved_chunks,
#     "answer": answer,
#     "audio_file": audio_url
# }


# @app.get("/get-audio/{filename}")
# async def get_audio(filename: str):
#     file_path = os.path.join("Data", "Audio", filename)
#     if os.path.exists(file_path):
#         return FileResponse(file_path, media_type="audio/mp3")
#     return {"error": "File not found"}


# from fastapi import FastAPI, File, UploadFile, Form
# from fastapi.responses import FileResponse
# from App.speech_to_text import convert_speech_to_text
# from fastapi import UploadFile, File

# import shutil
# import os

# from App.pdf2img import convert_pdf_to_image
# from App.ocr_tesseract import run_ocr_on_images
# from App.base64_utils import encode_pdf_to_base64, decode_base64_to_pdf
# from App.chunker import chunk_text_file
# from App.embed_store import create_embeddings_and_store
# from App.retriever import process_query_and_retrieve
# from App.llm_generator import generate_answer_with_gemini
# from App.web_search import get_web_search_results
# from App.text_to_speech import convert_text_to_speech

# app = FastAPI()

# # === Directories ===
# UPLOAD_DIR = os.path.join("Data", "Input_pdf_folder")
# TEXT_OUTPUT_DIR = os.path.join("Data", "Extracted_texts")
# CHUNK_DIR = os.path.join("Data", "Chunks")
# AUDIO_DIR = os.path.join("Data", "Audio")

# # Ensure directories exist
# os.makedirs(UPLOAD_DIR, exist_ok=True)
# os.makedirs(TEXT_OUTPUT_DIR, exist_ok=True)
# os.makedirs(CHUNK_DIR, exist_ok=True)
# os.makedirs(AUDIO_DIR, exist_ok=True)

# @app.post("/speech-to-text/")
# async def speech_to_text(audio: UploadFile = File(...)):
#     """
#     Converts uploaded audio to text for querying.
#     """
#     audio_path = os.path.join("Data", "Audio", audio.filename)
#     with open(audio_path, "wb") as buffer:
#         shutil.copyfileobj(audio.file, buffer)
    
#     text = convert_speech_to_text(audio_path)
    
#     return {"recognized_text": text}



# @app.post("/upload/")
# async def upload_file(file: UploadFile = File(...)):
#     print(" [INFO] Upload API called")

#     # === Step 1: Save uploaded PDF ===
#     pdf_filename = file.filename
#     original_pdf_path = os.path.join(UPLOAD_DIR, pdf_filename)
#     with open(original_pdf_path, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)
#     print(" [INFO] Original PDF saved successfully!")

#     # === Step 2: Encode PDF to Base64 ===
#     pdf_base64 = encode_pdf_to_base64(original_pdf_path)
#     print(" [INFO] PDF encoded to Base64.")

#     # === Step 3: Decode Base64 back to PDF ===
#     decoded_pdf_path = os.path.join(UPLOAD_DIR, f"decoded_{pdf_filename}")
#     decode_base64_to_pdf(pdf_base64, decoded_pdf_path)
#     print(" [INFO] PDF decoded successfully!")

#     # === Step 4: Prepare output text file path ===
#     base_filename = os.path.splitext(pdf_filename)[0]
#     output_text_path = os.path.join(TEXT_OUTPUT_DIR, f"{base_filename}.txt")

#     # === Step 5: Convert decoded PDF to Images ===
#     image_paths = convert_pdf_to_image(f"decoded_{pdf_filename}")
#     print(f" [INFO] Decoded PDF converted into {len(image_paths)} image(s).")

#     # === Step 6: Run OCR on Images ===
#     run_ocr_on_images(image_paths, output_text_path)
#     print(f" [INFO] OCR complete. Extracted text saved to: {output_text_path}")

#     # === Step 7: Chunk text ===
#     chunk_output_path = os.path.join(CHUNK_DIR, f"{base_filename}_chunks.txt")
#     num_chunks = chunk_text_file(output_text_path, chunk_output_path, chunk_size=1000)
#     print(f" [INFO] Created {num_chunks} chunks.")

#     # === Step 8: Create embeddings and store in ChromaDB ===
#     embedding_result = create_embeddings_and_store(chunk_output_path, collection_name=base_filename)
#     print(f" [INFO] Embeddings stored for {embedding_result['chunks_stored']} chunks")

#     return {
#         "message": "PDF processed and embeddings stored successfully",
#         "original_pdf": original_pdf_path,
#         "decoded_pdf": decoded_pdf_path,
#         "text_file": output_text_path,
#         "chunks_file": chunk_output_path,
#         "num_chunks": num_chunks,
#         "embeddings_info": embedding_result,
#         "total_pages": len(image_paths),
#         "base64_preview": pdf_base64[:50] + "..."
#     }


# @app.post("/query/")
# async def query_document(query: str = Form(...), collection_name: str = Form(...)):
#     """
#     Tries to answer from the PDF (RAG). If not found, fetch from web.
#     Also generates speech for the answer.
#     """
#     print(f"🔍 [INFO] Query received: {query}")

#     # Step 1: Retrieve relevant chunks
#     retrieved_chunks = process_query_and_retrieve(query, collection_name=collection_name, top_k=3)

#     # Step 2: Try generating answer using Gemini with PDF context
#     answer = generate_answer_with_gemini(query, retrieved_chunks)

#     # Step 3: If answer is empty or says 'not available', try web search
#     if "Based on the provided document, the answer is not available." in answer or not answer.strip():
#         print("[INFO] Answer not found in PDF. Searching the web...")
#         web_results = get_web_search_results(query)
#         answer = generate_answer_with_gemini(query, web_results)

#     # Step 4: Convert text to speech and save in AUDIO_DIR
#     audio_path = convert_text_to_speech(answer)
#     audio_url = f"http://localhost:8000/get-audio/{os.path.basename(audio_path)}"

#     return {
#     "query": query,
#     "retrieved_chunks": retrieved_chunks,
#     "answer": answer,
#     "audio_file": audio_url
# }


# @app.get("/get-audio/{filename}")
# async def get_audio(filename: str):
#     file_path = os.path.join("Data", "Audio", filename)
#     if os.path.exists(file_path):
#         return FileResponse(file_path, media_type="audio/mp3")
#     return {"error": "File not found"}






from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import FileResponse
from fastapi import UploadFile, File
import shutil
import os

from App.pdf2img import convert_pdf_to_image
from App.ocr_tesseract import run_ocr_on_images
from App.base64_utils import encode_pdf_to_base64, decode_base64_to_pdf
from App.chunker import chunk_text_file
from App.embed_store import create_embeddings_and_store
from App.retriever import process_query_and_retrieve
from App.llm_generator import generate_answer_with_gemini
from App.web_search import get_web_search_results
from App.text_to_speech import convert_text_to_speech
from App.speech_to_text import convert_speech_to_text

app = FastAPI()

# === Directories ===
UPLOAD_DIR = os.path.join("Data", "Input_pdf_folder")
TEXT_OUTPUT_DIR = os.path.join("Data", "Extracted_texts")
CHUNK_DIR = os.path.join("Data", "Chunks")
AUDIO_DIR = os.path.join("Data", "Audio")

# Ensure directories exist
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(TEXT_OUTPUT_DIR, exist_ok=True)
os.makedirs(CHUNK_DIR, exist_ok=True)
os.makedirs(AUDIO_DIR, exist_ok=True)

@app.post("/speech-to-text/")
async def speech_to_text(audio: UploadFile = File(...)):
    """
    Converts uploaded audio to text for querying.
    """
    audio_path = os.path.join("Data", "Audio", audio.filename)
    with open(audio_path, "wb") as buffer:
        shutil.copyfileobj(audio.file, buffer)
    
    text = convert_speech_to_text(audio_path)
    
    return {"recognized_text": text}



@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    print(" [INFO] Upload API called")

    # === Step 1: Save uploaded PDF ===
    pdf_filename = file.filename
    original_pdf_path = os.path.join(UPLOAD_DIR, pdf_filename)
    with open(original_pdf_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    print(" [INFO] Original PDF saved successfully!")

    # === Step 2: Encode PDF to Base64 ===
    pdf_base64 = encode_pdf_to_base64(original_pdf_path)
    print(" [INFO] PDF encoded to Base64.")

    # === Step 3: Decode Base64 back to PDF ===
    decoded_pdf_path = os.path.join(UPLOAD_DIR, f"decoded_{pdf_filename}")
    decode_base64_to_pdf(pdf_base64, decoded_pdf_path)
    print(" [INFO] PDF decoded successfully!")

    # === Step 4: Prepare output text file path ===
    base_filename = os.path.splitext(pdf_filename)[0]
    output_text_path = os.path.join(TEXT_OUTPUT_DIR, f"{base_filename}.txt")

    # === Step 5: Convert decoded PDF to Images ===
    image_paths = convert_pdf_to_image(f"decoded_{pdf_filename}")
    print(f" [INFO] Decoded PDF converted into {len(image_paths)} image(s).")

    # === Step 6: Run OCR on Images ===
    run_ocr_on_images(image_paths, output_text_path)
    print(f" [INFO] OCR complete. Extracted text saved to: {output_text_path}")

    # === Step 7: Chunk text ===
    chunk_output_path = os.path.join(CHUNK_DIR, f"{base_filename}_chunks.txt")
    num_chunks = chunk_text_file(output_text_path, chunk_output_path, chunk_size=1000)
    print(f" [INFO] Created {num_chunks} chunks.")

    # === Step 8: Create embeddings and store in ChromaDB ===
    embedding_result = create_embeddings_and_store(chunk_output_path, collection_name=base_filename)
    print(f" [INFO] Embeddings stored for {embedding_result['chunks_stored']} chunks")

    return {
        "message": "PDF processed and embeddings stored successfully",
        "original_pdf": original_pdf_path,
        "decoded_pdf": decoded_pdf_path,
        "text_file": output_text_path,
        "chunks_file": chunk_output_path,
        "num_chunks": num_chunks,
        "embeddings_info": embedding_result,
        "total_pages": len(image_paths),
        "base64_preview": pdf_base64[:50] + "..."
    }


@app.post("/query/")
async def query_document(query: str = Form(...), collection_name: str = Form(...)):
    """
    Tries to answer from the PDF (RAG). If not found, fetch from web.
    Also generates speech for the answer.
    """
    print(f"🔍 [INFO] Query received: {query}")

    # Step 1: Retrieve relevant chunks
    retrieved_chunks = process_query_and_retrieve(query, collection_name=collection_name, top_k=3)

    # Step 2: Try generating answer using Gemini with PDF context
    answer = generate_answer_with_gemini(query, retrieved_chunks)

    # Step 3: If answer is empty or says 'not available', try web search
    if "Based on the provided document, the answer is not available." in answer or not answer.strip():
        print("[INFO] Answer not found in PDF. Searching the web...")
        web_results = get_web_search_results(query)
        answer = generate_answer_with_gemini(query, web_results)

    # Step 4: Convert text to speech and save in AUDIO_DIR
    audio_path = convert_text_to_speech(answer)
    audio_url = f"http://localhost:8000/get-audio/{os.path.basename(audio_path)}"

    return {
    "query": query,
    "retrieved_chunks": retrieved_chunks,
    "answer": answer,
    "audio_file": audio_url
}


@app.get("/get-audio/{filename}")
async def get_audio(filename: str):
    file_path = os.path.join("Data", "Audio", filename)
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="audio/mp3")
    return {"error": "File not found"}
