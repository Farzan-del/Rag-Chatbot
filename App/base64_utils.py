# App/base64_utils.py
import base64

def encode_pdf_to_base64(pdf_path: str) -> str:
    """
    Reads a PDF file and returns its Base64 encoded string.
    """
    with open(pdf_path, "rb") as pdf_file:
        pdf_bytes = pdf_file.read()
    return base64.b64encode(pdf_bytes).decode("utf-8")


def decode_base64_to_pdf(base64_string: str, output_path: str) -> str:
    """
    Decodes a Base64 string and saves it as a PDF file at the specified path.
    Returns the output file path.
    """
    pdf_bytes = base64.b64decode(base64_string)
    with open(output_path, "wb") as pdf_file:
        pdf_file.write(pdf_bytes)
    return output_path
