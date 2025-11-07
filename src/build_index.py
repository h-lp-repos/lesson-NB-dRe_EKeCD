import os
import json
from dotenv import load_dotenv
import openai

def chunk_text(text, chunk_size=200):
    words = text.split()
    chunks = [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks

def generate_embeddings(chunks):
    model = os.getenv("EMBEDDING_MODEL")
    embeddings = []
    for chunk in chunks:
        response = openai.Embedding.create(input=chunk, model=model)
        embeddings.append(response["data"][0]["embedding"])
    return embeddings

def build_index(text, chunk_size=200):
    chunks = chunk_text(text, chunk_size)
    embeddings = generate_embeddings(chunks)
    return chunks, embeddings

if __name__ == "__main__":
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    # Read source document
    with open("data/faq_document.txt", "r") as f:
        text = f.read()
    # Build index
    chunks, embeddings = build_index(text, chunk_size=200)
    # Prepare index data
    index_data = [{"chunk": c, "embedding": e} for c, e in zip(chunks, embeddings)]
    # Save index to file
    os.makedirs("outputs", exist_ok=True)
    with open("outputs/index.json", "w") as f:
        json.dump(index_data, f, indent=2)
    print(f"Index built with {len(chunks)} chunks and saved to outputs/index.json")
