# import streamlit as st
# import requests

# # === Backend URL ===
# FASTAPI_URL = "http://localhost:8000"

# st.set_page_config(page_title="RAG Chat", page_icon="🤖", layout="wide")

# # === Initialize session state ===
# if "messages" not in st.session_state:
#     st.session_state.messages = []
# if "pdf_uploaded" not in st.session_state:
#     st.session_state.pdf_uploaded = False
# if "collection_name" not in st.session_state:
#     st.session_state.collection_name = None

# st.title("📚 RAG-Powered Chatbot with Audio")

# # === Upload PDF Section ===
# st.sidebar.header("Upload a PDF")

# if not st.session_state.pdf_uploaded:
#     uploaded_file = st.sidebar.file_uploader("Choose a PDF", type="pdf")
#     if uploaded_file is not None and st.sidebar.button("Process PDF"):
#         with st.spinner("Uploading and processing PDF..."):
#             files = {"file": uploaded_file}
#             response = requests.post(f"{FASTAPI_URL}/upload/", files=files)

#         if response.status_code == 200:
#             st.session_state.pdf_uploaded = True
#             st.session_state.collection_name = uploaded_file.name.replace(".pdf", "")
#             st.sidebar.success(f"✅ PDF processed successfully! Collection: {st.session_state.collection_name}")
#             st.sidebar.json(response.json())
#         else:
#             st.sidebar.error("❌ Error processing PDF")
# else:
#     st.sidebar.success(f"✅ PDF already processed: {st.session_state.collection_name}")
#     if st.sidebar.button("Reset"):
#         st.session_state.pdf_uploaded = False
#         st.session_state.collection_name = None
#         st.session_state.messages = []

# # === Chat Interface ===
# st.subheader("Ask a Question About Your Document")

# user_input = st.text_input("Type your question...")

# if st.button("Ask"):
#     if not user_input:
#         st.warning("Please enter a question.")
#     elif not st.session_state.collection_name:
#         st.warning("Please upload and process a PDF first.")
#     else:
#         # Add user message to chat history
#         st.session_state.messages.append({"role": "user", "content": user_input})

#         with st.spinner("Retrieving answer..."):
#             data = {"query": user_input, "collection_name": st.session_state.collection_name}
#             response = requests.post(f"{FASTAPI_URL}/query/", data=data)

#         if response.status_code == 200:
#             result = response.json()
#             answer = result.get("answer", "No answer found.")
#             audio_file = result.get("audio_file")  # ✅ Get audio file path from API

#             # Add AI response to chat history
#             st.session_state.messages.append({"role": "assistant", "content": answer, "audio": audio_file})
#         else:
#             st.error("Error querying the document.")

# # === Display Chat History ===
# for msg in st.session_state.messages:
#     if msg["role"] == "user":
#         st.markdown(f"**You:** {msg['content']}")
#     else:
#         st.markdown(f"**AI:** {msg['content']}")
#         # ✅ Play audio if available
#         if msg.get("audio"):
#             try:
#                 with open(msg["audio"], "rb") as f:
#                     st.audio(f.read(), format="audio/mp3")
#             except FileNotFoundError:
#                 st.warning("Audio file not found.")







# import streamlit as st
# import requests
# from audio_recorder_streamlit import audio_recorder  # For real-time mic recording

# # === Backend URL ===
# FASTAPI_URL = "http://localhost:8000"

# st.set_page_config(page_title="RAG Chat", page_icon="🤖", layout="wide")

# # === Initialize session state ===
# if "messages" not in st.session_state:
#     st.session_state.messages = []
# if "pdf_uploaded" not in st.session_state:
#     st.session_state.pdf_uploaded = False
# if "collection_name" not in st.session_state:
#     st.session_state.collection_name = None

# st.title("📚 RAG-Powered Chatbot with Voice")

# # === Upload PDF Section ===
# st.sidebar.header("Upload a PDF")

# if not st.session_state.pdf_uploaded:
#     uploaded_file = st.sidebar.file_uploader("Choose a PDF", type="pdf")
#     if uploaded_file is not None and st.sidebar.button("Process PDF"):
#         with st.spinner("Uploading and processing PDF..."):
#             files = {"file": uploaded_file}
#             response = requests.post(f"{FASTAPI_URL}/upload/", files=files)

#         if response.status_code == 200:
#             st.session_state.pdf_uploaded = True
#             st.session_state.collection_name = uploaded_file.name.replace(".pdf", "")
#             st.sidebar.success(f"✅ PDF processed successfully! Collection: {st.session_state.collection_name}")
#             st.sidebar.json(response.json())
#         else:
#             st.sidebar.error("❌ Error processing PDF")
# else:
#     st.sidebar.success(f"✅ PDF already processed: {st.session_state.collection_name}")
#     if st.sidebar.button("Reset"):
#         st.session_state.pdf_uploaded = False
#         st.session_state.collection_name = None
#         st.session_state.messages = []

# # === Chat Interface ===
# st.subheader("Ask a Question About Your Document")

# # === Text Input Option ===
# user_input = st.text_input("Type your question...")

# if st.button("Ask"):
#     if not user_input:
#         st.warning("Please enter a question.")
#     elif not st.session_state.collection_name:
#         st.warning("Please upload and process a PDF first.")
#     else:
#         st.session_state.messages.append({"role": "user", "content": user_input})

#         with st.spinner("Retrieving answer..."):
#             data = {"query": user_input, "collection_name": st.session_state.collection_name}
#             response = requests.post(f"{FASTAPI_URL}/query/", data=data)

#         if response.status_code == 200:
#             result = response.json()
#             answer = result.get("answer", "No answer found.")
#             audio_file = result.get("audio_file")  # Full URL from FastAPI
#             audio_url = audio_file if audio_file else None

#             st.session_state.messages.append({
#                 "role": "assistant",
#                 "content": answer,
#                 "audio": audio_url
#             })
#         else:
#             st.error("Error querying the document.")

# # === Voice Query Section (Fully Automated) ===
# st.subheader("🎤 Speak Your Question")

# audio_bytes = audio_recorder(text="Click to record", pause_threshold=2.0)

# if audio_bytes:
#     st.audio(audio_bytes, format="audio/wav")  # Optional playback for confirmation

#     with st.spinner("Processing your voice..."):
#         # Step 1: Convert speech to text
#         files = {"audio": ("voice.wav", audio_bytes, "audio/wav")}
#         response = requests.post(f"{FASTAPI_URL}/speech-to-text/", files=files)

#     if response.status_code == 200:
#         recognized_text = response.json().get("recognized_text", "")
#         st.write(f"**You said:** {recognized_text}")

#         # Step 2: Automatically query AI
#         if recognized_text.strip() and st.session_state.collection_name:
#             with st.spinner("Generating answer..."):
#                 data = {"query": recognized_text, "collection_name": st.session_state.collection_name}
#                 query_response = requests.post(f"{FASTAPI_URL}/query/", data=data)

#             if query_response.status_code == 200:
#                 result = query_response.json()
#                 answer = result.get("answer", "No answer found.")
#                 audio_file = result.get("audio_file")
#                 audio_url = audio_file if audio_file else None

#                 # Add to chat history
#                 st.session_state.messages.append({"role": "user", "content": recognized_text})
#                 st.session_state.messages.append({"role": "assistant", "content": answer, "audio": audio_url})
#             else:
#                 st.error("Error generating answer from RAG pipeline.")
#     else:
#         st.error("Failed to convert speech to text.")

# # === Display Chat History ===
# st.subheader("💬 Chat History")
# for msg in st.session_state.messages:
#     if msg["role"] == "user":
#         st.markdown(f"**You:** {msg['content']}")
#     else:
#         st.markdown(f"**AI:** {msg['content']}")

#         # ✅ Render Audio Player via HTML
#         if msg.get("audio"):
#             audio_html = f"""
#             <audio controls>
#                 <source src="{msg['audio']}" type="audio/mpeg">
#                 Your browser does not support the audio element.
#             </audio>
#             """
#             st.markdown(audio_html, unsafe_allow_html=True)

# best code till now without speech to text




# import streamlit as st
# import requests
# from audio_recorder_streamlit import audio_recorder  # ✅ Ensure this is installed
# from io import BytesIO

# # --- CONFIG ---
# FASTAPI_URL = "http://localhost:8000"
# st.set_page_config(page_title="📚 RAG Chatbot with Voice", layout="wide")
# st.title("📚 RAG-Powered Chatbot with Audio & Voice")

# # --- SESSION STATE ---
# if "messages" not in st.session_state:
#     st.session_state.messages = []
# if "collection_name" not in st.session_state:
#     st.session_state.collection_name = "default"

# # --- FILE UPLOAD ---
# st.subheader("📄 Upload PDF (optional)")
# uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
# if uploaded_file:
#     with st.spinner("Uploading and processing PDF..."):
#         files = {"file": (uploaded_file.name, uploaded_file, "application/pdf")}
#         response = requests.post(f"{FASTAPI_URL}/upload-pdf/", files=files)
#         if response.status_code == 200:
#             result = response.json()
#             st.success("PDF uploaded and processed.")
#             st.session_state.collection_name = result.get("collection_name", "default")
#         else:
#             st.error("Failed to upload PDF.")

# # --- INPUT TEXT OR AUDIO ---
# st.subheader("💬 Ask a Question")
# user_input = st.text_input("Type your question:", key="text_input")

# use_mic = st.checkbox("🎤 Use Mic to Ask")
# if use_mic:
#     audio_bytes = audio_recorder(pause_threshold=1.0)
#     if audio_bytes:
#         st.audio(audio_bytes, format="audio/wav")
#         st.info("Transcribing your audio...")
#         files = {"audio": ("query.wav", audio_bytes, "audio/wav")}
#         resp = requests.post(f"{FASTAPI_URL}/speech-to-text/", files=files)
#         if resp.status_code == 200:
#             text = resp.json().get("recognized_text", "")
#             st.success(f"Recognized: **{text}**")
#             user_input = text
#         else:
#             st.error("Speech-to-text failed.")

# # --- SUBMIT QUERY ---
# if st.button("Ask"):
#     if not user_input:
#         st.warning("Please enter or speak your question first.")
#     else:
#         # Save user message
#         st.session_state.messages.append({"role": "user", "content": user_input})

#         # Query backend
#         with st.spinner("Querying backend..."):
#             data = {
#                 "query": user_input,
#                 "collection_name": st.session_state.get("collection_name", "default")
#             }
#             r = requests.post(f"{FASTAPI_URL}/query/", data=data)

#         if r.status_code == 200:
#             result = r.json()
#             answer = result.get("answer", "")
#             audio_url = result.get("audio_file")

#             # Append assistant message
#             st.session_state.messages.append({
#                 "role": "assistant",
#                 "content": answer,
#                 "audio": audio_url
#             })
#         else:
#             st.error("Backend query failed.")

# # --- DISPLAY CHAT HISTORY ---
# st.subheader("💬 Chat History")
# for i, msg in enumerate(st.session_state.messages):
#     if msg["role"] == "user":
#         st.markdown(f"**🧑 You:** {msg['content']}")
#     else:
#         st.markdown(f"**🤖 AI:** {msg['content']}")
#         if msg.get("audio"):
#             try:
#                 audio_response = requests.get(msg["audio"])
#                 if audio_response.status_code == 200:
#                     st.audio(BytesIO(audio_response.content))
#                 else:
#                     st.warning("Audio fetch failed.")
#             except:
#                 st.warning("Couldn't load audio.")

# best code but file upload is not working only

import streamlit as st
import requests
from audio_recorder_streamlit import audio_recorder
from io import BytesIO

# === CONFIG ===
FASTAPI_URL = "http://localhost:8000"
st.set_page_config(page_title="📚 RAG Voice Chatbot", layout="wide")
st.title("📚 RAG-Powered Chatbot with Audio & Voice")

# === SESSION STATE ===
if "messages" not in st.session_state:
    st.session_state.messages = []
if "pdf_uploaded" not in st.session_state:
    st.session_state.pdf_uploaded = False
if "collection_name" not in st.session_state:
    st.session_state.collection_name = None

# === SIDEBAR: Upload PDF ===
st.sidebar.header("📄 Upload a PDF")

if not st.session_state.pdf_uploaded:
    uploaded_file = st.sidebar.file_uploader("Choose a PDF", type="pdf")
    if uploaded_file and st.sidebar.button("📤 Process PDF"):
        with st.spinner("Uploading and indexing your PDF..."):
            files = {"file": uploaded_file}
            response = requests.post(f"{FASTAPI_URL}/upload/", files=files)

        if response.status_code == 200:
            st.session_state.pdf_uploaded = True
            st.session_state.collection_name = uploaded_file.name.replace(".pdf", "")
            st.sidebar.success(f"✅ PDF processed: {st.session_state.collection_name}")
            st.sidebar.json(response.json())
        else:
            st.sidebar.error("❌ Failed to process PDF.")
else:
    st.sidebar.success(f"✅ PDF loaded: {st.session_state.collection_name}")
    if st.sidebar.button("🔁 Reset"):
        st.session_state.pdf_uploaded = False
        st.session_state.collection_name = None
        st.session_state.messages = []

# === MAIN CHAT INTERFACE ===
st.subheader("💬 Ask a Question")

user_input = st.text_input("Type your question...", key="text_input")

use_mic = st.checkbox("🎤 Use Mic Instead")
if use_mic:
    audio_bytes = audio_recorder(pause_threshold=1.0)
    if audio_bytes:
        st.audio(audio_bytes, format="audio/wav")
        st.info("Transcribing audio to text...")
        files = {"audio": ("query.wav", audio_bytes, "audio/wav")}
        resp = requests.post(f"{FASTAPI_URL}/speech-to-text/", files=files)
        if resp.status_code == 200:
            user_input = resp.json().get("recognized_text", "")
            st.success(f"Recognized: **{user_input}**")
        else:
            st.error("Speech-to-text failed.")

# === ASK BUTTON ===
if st.button("🚀 Ask"):
    if not user_input:
        st.warning("Please enter or speak a question.")
    elif not st.session_state.collection_name:
        st.warning("Upload and process a PDF first.")
    else:
        # Add user message
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Send to backend
        with st.spinner("Retrieving answer..."):
            payload = {
                "query": user_input,
                "collection_name": st.session_state.collection_name
            }
            response = requests.post(f"{FASTAPI_URL}/query/", data=payload)

        if response.status_code == 200:
            result = response.json()
            answer = result.get("answer", "No answer received.")
            audio_url = result.get("audio_file")

            # Add assistant response
            st.session_state.messages.append({
                "role": "assistant",
                "content": answer,
                "audio": audio_url
            })
        else:
            st.error("❌ Backend query failed.")

# === CHAT HISTORY DISPLAY ===
st.subheader("📝 Chat History")

for idx, msg in enumerate(st.session_state.messages):
    if msg["role"] == "user":
        st.markdown(f"**🧑 You:** {msg['content']}")
    else:
        st.markdown(f"**🤖 AI:** {msg['content']}")
        if msg.get("audio"):
            try:
                audio_resp = requests.get(msg["audio"])
                if audio_resp.status_code == 200:
                    st.audio(BytesIO(audio_resp.content))
                else:
                    st.warning("⚠️ Couldn't fetch audio.")
            except Exception as e:
                st.warning(f"Audio error: {e}")
