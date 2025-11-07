import json

def test_sample_queries_structure():
    data = json.load(open("outputs/sample_queries.json"))
    assert isinstance(data, list)
    assert len(data) >= 3
    for item in data[:3]:
        assert "user_question" in item
        assert "answer" in item
        assert "sources" in item
        assert "scores" in item
        assert isinstance(item["sources"], list)
        assert isinstance(item["scores"], list)
