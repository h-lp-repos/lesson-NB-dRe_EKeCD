import os
import openai
from src.build_index import generate_embeddings

def test_generate_embeddings(monkeypatch):
    dummy_chunks = ["chunk one", "chunk two"]
    expected = [0.1, 0.2, 0.3]
    def dummy_create(input, model):
        return {"data": [{"embedding": expected}]}
    monkeypatch.setattr(openai.Embedding, "create", dummy_create)
    monkeypatch.setenv("EMBEDDING_MODEL", "test-model")
    embeddings = generate_embeddings(dummy_chunks)
    assert isinstance(embeddings, list)
    assert embeddings == [expected, expected]
    for emb in embeddings:
        assert isinstance(emb, list)
        assert len(emb) == len(expected)
