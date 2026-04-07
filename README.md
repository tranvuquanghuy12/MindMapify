<div align="center">
<h1>MindMapify: Context-Aware Semantic Knowledge Mapping <br>for Visual Vocabulary Acquisition</h1>

**A Research & Development Project by Trần Vũ Quang Huy**
<br>
*Bridging the Gap between Plain Text and Interactive Knowledge Graphs in Modern Education*

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-Vite-61DAFB.svg)](https://reactjs.org/)
[![BERT](https://img.shields.io/badge/NLP_Engine-BERT_Embeddings-fdc500.svg)](https://huggingface.co/)
[![DALL-E 3](https://img.shields.io/badge/GenAI-DALL--E_3-black.svg)](https://openai.com/)

</div>

---

## 📌 Project Overview

**MindMapify** is an advanced AI-powered Semantic Knowledge Mapping framework designed for **Visual-driven Language Exploration**. It transforms static vocabulary lists into dynamic, interactive 2D networks, enabling users to explore semantic relationships between English words effortlessly.

### 🔍 The Problem: Rote Memorization
In traditional language learning, vocabulary acquisition often suffers from:
1. **Lack of Context**: Words are learned in isolation, ignoring the rich semantic connections between related concepts.
2. **Poor Retention**: Text-heavy flashcards fail to engage visual learners, leading to a drop in long-term memory retention.

### 💡 The MindMapify Solution
Our system introduces a **Semantic Entity Discovery engine** combined with **Generative Multi-modal Interaction**:
- **Semantic Clustering**: Automatically groups related concepts using BERT-based embeddings to establish high-level correlations between words.
- **Generative Visual Synthesis**: Utilizes DALL-E 3 to synthesize dynamic, visually striking flashcards and contextual illustrations on demand.
- **Interactive Knowledge Graph**: Provides a fluid, draggable 2D workspace where users can visually trace the latent semantic dependencies between vocabulary nodes.

---

## 🛠️ Tech Stack & Architecture
- **NLP Engine**: BERT Embeddings, Real-time Named Entity Recognition (NER) via spaCy.
- **Generative AI**: OpenAI DALL-E 3 for multi-modal visual synthesis.
- **Backend Infrastructure**: FastAPI (Python) optimized for asynchronous AI inference and vector processing.
- **Frontend Ecosystem**: React (Vite) for high-performance, real-time graph rendering.

---

## 🚀 Execution Guide

### 1. Data Preparation (Semantic Embeddings)
To generate the initial semantic correlations between the dictionary vocabulary:
```bash
cd backend
# Note: The first execution downloads the BERT model weights (~400MB)
python process_dictionary.py
```

### 2. Service Initialization
Launch the core inference API and the interactive visualization platform:
```bash
# Terminal 1: Backend Server (Port 8000)
cd backend
python main.py

# Terminal 2: Frontend Environment (Port 5173)
cd frontend
npm run dev
```

### 3. Docker Deployment (Cloud Ready)
Deploy the entire microservice architecture using Docker Compose:
```bash
docker-compose up --build
```

---

## 📁 Repository Organization
- `backend/nlp_engine.py`: Core implementation of the BERT-based Semantic Graph extraction.
- `backend/image_gen.py`: Generative synthesis module interfacing with DALL-E 3.
- `backend/process_dictionary.py`: Preprocessing logic for dictionary datasets.
- `frontend/src/`: React components for handling Context-Aware Graph Rendering.

---
*Developed as a modern solution for EdTech and Interactive Learning. For collaboration or inquiries, please reach out via GitHub or LinkedIn.*
