import pytest
from src.build_index import chunk_text

def test_chunk_count():
    with open("data/faq_document.txt", "r") as f:
        text = f.read()
    chunks = chunk_text(text, chunk_size=50)
    assert len(chunks) >= 20, f"Expected at least 20 chunks, got {len(chunks)}"
