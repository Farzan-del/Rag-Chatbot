# App/chunker.py
import os

def chunk_text_file(input_file: str, output_file: str, chunk_size: int = 1000):
    """
    Reads a text file, splits it into character-based chunks,
    and writes them into a new file (one chunk per line).
    """
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file not found: {input_file}")

    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        for chunk in chunks:
            f.write(chunk.strip() + "\n---CHUNK---\n")

    return len(chunks)
