import openai
from src.query import answer_question

def test_answer_question(monkeypatch):
    dummy_embedding = [0.1] * 5
    dummy_index = [{"chunk": "c1", "embedding": dummy_embedding}, {"chunk": "c2", "embedding": dummy_embedding}]
    def dummy_emb_create(input, model):
        return {"data": [{"embedding": dummy_embedding}]}
    monkeypatch.setattr(openai.Embedding, "create", dummy_emb_create)
    def dummy_chat_create(model, messages):
        class Choice:
            def __init__(self):
                self.message = type("x", (), {"content": "test answer"})
        return type("resp", (), {"choices": [Choice()]})
    monkeypatch.setattr(openai.ChatCompletion, "create", dummy_chat_create)
    result = answer_question("test?", dummy_index, k=1)
    assert "answer" in result
    assert "sources" in result
    assert "scores" in result
    assert isinstance(result["sources"], list)
    assert isinstance(result["scores"], list)
    assert result["answer"] == "test answer"
