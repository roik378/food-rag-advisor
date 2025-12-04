# 🥗 Intelligent Dietary Recommendation Engine (RAG-Based)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://你的HuggingFace或GCP链接)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![Docker](https://img.shields.io/badge/docker-automated-blue)](https://www.docker.com/)

An AI-powered nutrition consultant built for the Shenzhen Futian area. It utilizes **Retrieval-Augmented Generation (RAG)** to provide personalized restaurant recommendations based on user health metrics (e.g., post-workout, fat loss).

## 🚀 Key Features

* **RAG Architecture:** Combines Google's **Gemini Pro** LLM with local vector retrieval to ensure recommendations are grounded in real-world data (restaurants.csv).
* **Vector Search:** Implemented using `sentence-transformers` and Cosine Similarity for high-precision semantic matching.
* **Serverless Deployment:** Fully containerized with **Docker** and deployed on **Google Cloud Run** (or Hugging Face Spaces), featuring auto-scaling capabilities.
* **DevOps Ready:** Integrated CI/CD pipeline via GitHub Actions for automated testing and deployment.

## 🛠️ Tech Stack

* **LLM:** Google Gemini API
* **Vector DB:** FAISS / Local Embeddings (NumPy)
* **Frontend:** Streamlit
* **Containerization:** Docker & Cloud Run

## ⚡ Quick Start

### 1. Clone the repo
bash
git clone [https://github.com/你的用户名/food-rag-advisor.git](https://github.com/你的用户名/food-rag-advisor.git)
cd food-rag-advisor

2. Set up environment variables
Create a .env file and add your Google API Key:

GOOGLE_API_KEY=your_api_key_here
3. Run with Docker
Bash

docker build -t food-advisor .
docker run -p 8501:8501 food-advisor
