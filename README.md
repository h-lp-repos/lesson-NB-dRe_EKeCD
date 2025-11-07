# Assignment P2: FAQ Support Chatbot (RAG-Based)

This repository contains the starter code and resources for the **Andela GEN AI Program — Assignment P2**.
Students will build a Retrieval-Augmented Generation (RAG) based FAQ support chatbot to answer questions from a plain text document.

## Repository Structure

```text
.
├── data/
│   └── faq_document.txt
├── src/
│   ├── build_index.py
│   └── query.py
├── outputs/
│   └── sample_queries.json
├── .env.example
├── requirements.txt
└── README.md
```

## 📋 Checklist

- [ ] `data/faq_document.txt` (≥1000 words plain text FAQ document)
- [ ] `src/build_index.py` (chunking + embedding index builder)
- [ ] `src/query.py` (interactive query pipeline)
- [ ] `outputs/sample_queries.json` (≥3 sample query–response examples)
- [ ] `.env.example` (template for environment variables)
- [ ] `requirements.txt` (Python dependencies)
- [ ] Automated tests (in `tests/`) for index, embeddings, and query pipeline
- [ ] `CONTRIBUTING.md` (submission guidelines)
- [ ] `scripts/run_tests.sh` (helper script to run tests)

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone <repo_url>
   cd lesson-NB-dRe_EKeCD
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy environment variables:
   ```bash
   cp .env.example .env
   ```

## ⚙️ Running the Pipeline

### Build the index

Generate embeddings and build the index:
```bash
python src/build_index.py
```

### Query the chatbot

Run the interactive query interface:
```bash
python src/query.py
```

## 🧪 Running Tests

To execute automated tests:
```bash
./scripts/run_tests.sh
```

Expected output:
- All tests should pass, verifying chunking, embedding generation, and query pipeline outputs.
- Sample queries smoke tests to validate JSON structure.

## 📊 Data Provenance & Chunking Strategy

- Source document: `data/faq_document.txt` contains company FAQ topics (policies, procedures, features).
- Chunking: We split text into chunks of ~200 words to ensure at least 20 chunks and balance context size with embedding limits.
- Embeddings: Generated using the OpenAI `text-embedding-3-small` model (or configured via `EMBEDDING_MODEL`).

## 🔧 Component Implementation Details

| Component        | Implementation                                |
| ---------------- | --------------------------------------------- |
| Chunking         | Manual word-based splitting (`chunk_text`)    |
| Embedding Gen.   | Direct OpenAI Embeddings API (`openai.Embedding.create`) |
| Indexing         | JSON index file storing chunks and embeddings |
| Retrieval        | Cosine similarity k-NN search (numpy)         |
| Prompting        | Basic context injection with GPT-3.5-Turbo    |

Framework usage:
- **OpenAI Python SDK** is used for embedding and LLM inference.
- No high-level RAG frameworks are used for core steps to ensure transparency.
