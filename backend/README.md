# Document Intelligence System (RAG Backend)

A Django REST API-based project that implements a **basic Retrieval-Augmented Generation (RAG) architecture** for answering user queries.

---

## Project Overview

This project provides a simple backend API where users can send a query and receive a response.

It simulates a **RAG (Retrieval-Augmented Generation) pipeline**, where the retrieval layer is currently a placeholder and will be upgraded in the future with vector search and AI embeddings.

---

##  Features

- REST API for asking questions
- Query validation and error handling
- Modular backend structure (views, vector_store)
- Basic RAG-style architecture (placeholder retrieval)
- JSON request/response system

---

## 🔧 API Endpoint

### Ask Question API

**URL:**
POST /api/ask/


**Request Body:**
```json
{
  "query": "What is Django?"
}

Response:

{
  "query": "What is Django?",
  "answer": "Search function not implemented yet. You asked: What is Django?"
}
🛠 Tech Stack
Python
Django
Django REST Framework
📌 Project Status
Backend API: ✅ Completed
RAG Logic: ⚠️ Placeholder (not full AI yet)
Vector Database: ❌ Not implemented
Frontend: ❌ Not included