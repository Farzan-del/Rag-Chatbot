# # App/llm_generator.py
# import google.generativeai as genai
# import os

# # Set Gemini API Key
# genai.configure(api_key="AIzaSyCcR-EqAUO9d2st5FvUYjHGg3b1DtsU7lo")

# def generate_answer_with_gemini(query: str, context_chunks: list) -> str:
#     """
#     Combines retrieved chunks into a single context and uses Gemini to generate an answer.
#     """
#     context_text = "\n\n".join(context_chunks)
#     prompt = f"""
#     You are a helpful AI assistant. Answer the question based on the context provided.
    
#     Context:
#     {context_text}
    
#     Question:
#     {query}
    
#     Provide a clear and concise answer.
#     """

#     try:
#         model = genai.GenerativeModel("gemini-1.5-flash")
#         response = model.generate_content(prompt)
#         return response.text
#     except Exception as e:
#         return f"Error generating answer: {str(e)}"


# App/llm_generator.py
import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyCcR-EqAUO9d2st5FvUYjHGg3b1DtsU7lo")

def generate_answer_with_gemini(query: str, context_chunks: list) -> str:
    """
    If context is relevant, use it; otherwise, answer generally.
    """
    model = genai.GenerativeModel("gemini-1.5-flash")

    if context_chunks and len(" ".join(context_chunks).strip()) > 50:
        # RAG mode
        context_text = "\n\n".join(context_chunks)
        prompt = f"""
        You are a helpful AI assistant. Answer the question using the context provided below.
        
        Context:
        {context_text}
        
        Question:
        {query}
        
        If the context does not contain the answer, then politely say: "Based on the provided document, the answer is not available."
        """
    else:
        # General Knowledge mode
        prompt = f"""
        You are a knowledgeable assistant. Answer the following question accurately:

        Question:
        {query}
        """
    


    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating answer: {str(e)}"

