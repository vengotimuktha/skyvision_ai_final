# SkyVision AI – Intelligent Document Q&A System

SkyVision AI is an advanced Retrieval-Augmented Generation (RAG) system designed to intelligently answer questions based on the contents of uploaded PDF and CSV documents. It uses LangChain for text processing, OpenAI for embeddings and LLM responses, and FAISS for high-speed semantic search. The system is containerized using Docker and deployed on Google Cloud Platform (GCP), making it scalable and production-ready.

## Project Highlights

- Multi-format document support: PDF and CSV
- Text chunking and semantic indexing using LangChain
- Embedding generation via OpenAI
- Fast vector search with FAISS
- Natural language answers using GPT-3.5
- Modular and extensible architecture
- Secure API key management using `.env` or `secrets.toml`
- Dockerized and deployed on GCP Cloud Run

## Tech Stack

| Component               | Technology                            |
|------------------------|----------------------------------------|
| Frontend/UI            | Streamlit                              |
| LLM & Embeddings       | OpenAI GPT-3.5 Turbo, OpenAIEmbeddings |
| Document Parsing       | PyPDF2, pandas                         |
| Vector Store           | FAISS                                  |
| Text Splitting         | LangChain RecursiveCharacterTextSplitter |
| Deployment             | Docker, GCP Cloud Run                  |
| Secure Secrets         | .env or Streamlit secrets.toml         |

## Screenshots

| Uploading & Indexing            | Question Answering Interface     |
|----------------------------------|----------------------------------|
| ![Upload](./screenshots/upload_example.png) | ![QA](./screenshots/qa_example.png) |

## Directory Structure

skyvision_ai/
│
├── app.py                      # Streamlit frontend (UI)
├── utils.py                    # Core logic (indexing, retrieval)
├── embed_store.py              # Script for static text FAISS indexing
│
├── data/
│   ├── input/                  # Uploaded PDFs/CSVs
│   ├── extracted/              # Extracted raw text
│   └── skyvision_faiss_index/ # Stored FAISS indexes
│
├── .env                        # OpenAI key for local dev
├── .streamlit/secrets.toml    # Secrets for Streamlit Cloud (optional)
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Container setup for GCP deployment
└── README.md                  # Project documentation


## Local Development Setup

Follow these steps to set up and run the application locally:

### 1. Clone the Repository


git clone https://github.com/vengotimuktha/skyvision_ai_final.git
cd skyvision_ai

### 2. Set Up Virtual Environment

python -m venv venv
venv\Scripts\activate        # On Windows
source venv/bin/activate  # On Mac/Linux

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Add Your OpenAI API Key

Create a .env file in the root directory:
OPENAI_API_KEY=your-openai-key-here

Alternatively, use .streamlit/secrets.toml:
[general]
OPENAI_API_KEY = "your-openai-key-here"

### 5. Run the Application

streamlit run app.py

### GCP Deployment Overview
The application is containerized using Docker and deployed to Google Cloud Platform (Cloud Run). The cloud version includes:

Dockerized backend with automatic build

Secrets managed securely using GCP Secret Manager

Deployed to Cloud Run with auto-scaling and health checks

Exposed endpoint for real-time document Q&A in production

Deployment ensures low latency, scalability, and high availability for enterprise use cases.

### RAG System Architecture
[ User Uploads PDF/CSV ]
           ↓
[ Text Extraction ]
           ↓
[ Text Chunking via LangChain ]
           ↓
[ Embedding Generation (OpenAI) ]
           ↓
[ Semantic Indexing with FAISS ]
           ↓
[ User Asks Query ]
           ↓
[ Retrieve Top-k Chunks (FAISS) ]
           ↓
[ GPT-3.5 Turbo → Answer Generation ]
           ↓
[ Return Answer + Source Chunks ]

## Author

**Mukthasree Vengoti**  
GenAI Engineer |  Reality AI Lab  
 Portfolio: [https://datascienceportfol.io/mukthasreevengoti](https://datascienceportfol.io/mukthasreevengoti)  
 LinkedIn: [https://www.linkedin.com/in/mukthasree-vengoti](https://www.linkedin.com/in/mukthasree-vengoti)
