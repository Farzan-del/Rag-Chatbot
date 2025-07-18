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


import streamlit as st
import requests

# === Backend URL ===
FASTAPI_URL = "http://localhost:8000"

st.set_page_config(page_title="RAG Chat", page_icon="🤖", layout="wide")

# === Initialize session state ===
if "messages" not in st.session_state:
    st.session_state.messages = []
if "pdf_uploaded" not in st.session_state:
    st.session_state.pdf_uploaded = False
if "collection_name" not in st.session_state:
    st.session_state.collection_name = None

st.title("📚 RAG-Powered Chatbot with Voice")

# === Upload PDF Section ===
st.sidebar.header("Upload a PDF")

if not st.session_state.pdf_uploaded:
    uploaded_file = st.sidebar.file_uploader("Choose a PDF", type="pdf")
    if uploaded_file is not None and st.sidebar.button("Process PDF"):
        with st.spinner("Uploading and processing PDF..."):
            files = {"file": uploaded_file}
            response = requests.post(f"{FASTAPI_URL}/upload/", files=files)

        if response.status_code == 200:
            st.session_state.pdf_uploaded = True
            st.session_state.collection_name = uploaded_file.name.replace(".pdf", "")
            st.sidebar.success(f"✅ PDF processed successfully! Collection: {st.session_state.collection_name}")
            st.sidebar.json(response.json())
        else:
            st.sidebar.error("❌ Error processing PDF")
else:
    st.sidebar.success(f"✅ PDF already processed: {st.session_state.collection_name}")
    if st.sidebar.button("Reset"):
        st.session_state.pdf_uploaded = False
        st.session_state.collection_name = None
        st.session_state.messages = []

# === Chat Interface ===
st.subheader("Ask a Question About Your Document")

user_input = st.text_input("Type your question...")

if st.button("Ask"):
    if not user_input:
        st.warning("Please enter a question.")
    elif not st.session_state.collection_name:
        st.warning("Please upload and process a PDF first.")
    else:
        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.spinner("Retrieving answer..."):
            data = {"query": user_input, "collection_name": st.session_state.collection_name}
            response = requests.post(f"{FASTAPI_URL}/query/", data=data)

        if response.status_code == 200:
            result = response.json()
            answer = result.get("answer", "No answer found.")
            audio_file = result.get("audio_file")  # This should be the filename from FastAPI (e.g., response.mp3)

            # Build audio URL using FastAPI endpoint
            audio_url = audio_file if audio_file else None

            st.session_state.messages.append({
                "role": "assistant",
                "content": answer,
                "audio": audio_url
            })
        else:
            st.error("Error querying the document.")

# === Display Chat History ===
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**AI:** {msg['content']}")

        # ✅ Render Audio Player via HTML (better browser compatibility)
        if msg.get("audio"):
            audio_html = f"""
            <audio controls>
                <source src="{msg['audio']}" type="audio/mpeg">
                Your browser does not support the audio element.
            </audio>
            """
            st.markdown(audio_html, unsafe_allow_html=True)
