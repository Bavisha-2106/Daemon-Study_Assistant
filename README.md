# Daemon

A RAG-based study assistant that answers strictly from your own notes — not from general AI knowledge.

## What it does
Daemon reads your lecture notes (PDFs), stores them in a vector database, and answers your questions strictly from that content. If something isn't in your notes, it tells you. No hallucinations, no general knowledge leaking in.

## How it works
1. Your PDFs are split into chunks and stored in ChromaDB
2. When you ask a question, Daemon rewrites your query for better search accuracy
3. The most relevant chunks are retrieved and sent to the LLM
4. The LLM answers strictly from those chunks and cites the source

## Features
- Multi-PDF support
- Query rewriting for better retrieval
- Source citation on every answer
- Prompt injection resistant

## Known Limitations
- Retrieval can be inconsistent on vague follow-up queries
- Knowledge leakage from base LLM on some responses
- CLI only, no UI
- Free tier Groq API limits daily token usage
- No persistent chat history — each session starts fresh

## Setup
1. Clone the repo
2. Install dependencies: `pip install groq chromadb pypdf2`
3. Set your Groq API key: `$env:GROQ_API_KEY="your_key_here"`
4. Add your PDF notes to the project folder
5. Update the PDF filenames in `main.py`
6. Run: `python main.py`

## Tech Stack
- Groq API (LLaMA 3.3 70B)
- ChromaDB
- PyPDF2
- Python
