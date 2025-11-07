import os
import json
from dotenv import load_dotenv
import openai
import numpy as np

def load_index(path="outputs/index.json"):
    with open(path, "r") as f:
        return json.load(f)

def get_embedding(text):
    model = os.getenv("EMBEDDING_MODEL")
    response = openai.Embedding.create(input=text, model=model)
    return response["data"][0]["embedding"]

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def answer_question(question, index, k=5):
    q_emb = get_embedding(question)
    scores = []
    for item in index:
        score = cosine_similarity(q_emb, item["embedding"])
        scores.append({"chunk": item["chunk"], "score": score})
    top = sorted(scores, key=lambda x: x["score"], reverse=True)[:k]
    sources = [item["chunk"] for item in top]
    scores_only = [item["score"] for item in top]
    context = "\n\n".join(sources)
    prompt = f"Use the following context to answer the question: {question}\n\nContext:\n{context}\n\nAnswer:"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    answer = response.choices[0].message.content
    return {
        "user_question": question,
        "answer": answer,
        "sources": sources,
        "scores": scores_only
    }

if __name__ == "__main__":
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    index = load_index()
    question = input("Enter your question: ")
    result = answer_question(question, index)
    print(json.dumps(result, indent=2))
