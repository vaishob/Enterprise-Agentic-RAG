# Enterprise IT Agentic RAG

A local-first, agentic Retrieval-Augmented Generation system for enterprise IT knowledge bases — no cloud dependencies required for the core pipeline.

> **Status:** early scaffolding. This README is a preview of what's coming — code lands in upcoming commits.

## What's coming

- **Ingestion pipeline** — parse PDFs, DOCX, PPTX, and HTML docs (via `unstructured`, `pypdf`, `pdfplumber`, `python-docx`/`pptx`) into clean, chunked text.
- **Retrieval** — Gemini embeddings + Qdrant vector store, with FlashRank cross-encoder reranking for higher-precision results.
- **Agentic orchestration** — LangGraph-driven agent flows on top of LangChain, with Groq (Llama 3.3) and a Portkey gateway for unified LLM routing/fallbacks.
- **Guardrails** — NVIDIA NeMo Guardrails for input/output safety checks.
- **API + UI** — FastAPI backend, Streamlit chat frontend.
- **Observability** — LangSmith tracing, Logfire, and Loguru logging.
- **Evaluation** — RAGAS + DeepEval for faithfulness/relevancy/recall metrics, Langfuse for live production monitoring and feedback.

## Data

`DATA/true_data` holds the target enterprise-IT corpus (job orchestration, monitoring, scheduling, parallelism, worker scaling). `DATA/noisy_data` is a large distractor corpus used to stress-test retrieval precision against irrelevant documents.

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env  # fill in your API keys
```

More to come.
