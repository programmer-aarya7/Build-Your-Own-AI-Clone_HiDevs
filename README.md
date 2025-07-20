# Say Hi to  Askie 🤖: Your Personalized AI Clone Chatbot (RAG + Mistral + FAISS)

> 📚 Upload. 🌐 Link. ❓ Ask. 💡 Answer.  
> Meet **Askie** – your curious companion, not just a bot but your knowledge champion!

---

## 🎵 Who is Askie? 
Have a doc or link to scan?  
Askie's here to lend a hand.  
PDF or a website page,  
She’ll read it all, word by phrase.

---

##  What Askie Does

Askie is a **Retrieval-Augmented Generation (RAG)** based chatbot that allows users to:

- 1. Upload a **PDF** or enter a **URL**
- 2. Automatically **chunk and vectorize** the content using **FAISS + HuggingFace Embeddings**
- 3. Build a **retrieval chain** that fetches relevant chunks based on your queries
- 4. Generate **natural, contextual answers** using the **Mistral model via Ollama**
- 5. View the exact **source documents** used to answer your query
- 6. Optionally **log interactions** using **Arize AI** for observability

---

##  Tech Stack

| Component       | Tech Used                          |
|----------------|------------------------------------|
| LLM             | Mistral via Ollama (Local)         |
| Embeddings      | `sentence-transformers/all-MiniLM-L6-v2` |
| Vector Store    | FAISS                             |
| Chunking        | RecursiveCharacterTextSplitter     |
| PDF Parsing     | PyPDFLoader                        |
| Web Scraping    | WebBaseLoader                      |
| Frontend        | Streamlit                          |
| Observability   | Arize AI (optional)                |

---

## 📁 Project Structure
``` bash
Askie/
├── app.py              # Streamlit frontend
├── rag_pipeline.py     # RAG chain logic
├── utils/
│   └── chunking.py     # Chunking logic for PDF & URLs
├── .env                # Arize API keys and configs (should be excluded from GitHub)
├── data/               # Uploaded PDF files (usually excluded or kept empty)
└── README.md           # Project documentation
```
---

##  How Askie Works (Step-by-Step)

### 1️⃣ Upload or Input
- Upload a `.pdf` file OR enter a webpage URL.
- Askie reads and parses the content.

### 2️⃣ Chunk and Vectorize
- The content is chunked into small segments using `RecursiveCharacterTextSplitter`.
- Each chunk is converted into vector embeddings using `HuggingFaceEmbeddings`.

### 3️⃣ Build RAG Pipeline
- Chunks are stored in a FAISS vector store.
- A retriever fetches the most relevant chunks when a question is asked.
- Mistral LLM via Ollama generates an answer based on these chunks.

### 4️⃣ Chat and Source Tracking
- Askie responds to your question in natural language.
- Displays **source document chunks** used in the response.
- (Optional) Logs prompt, response, and metadata to **Arize**.

---

##  Local Setup

###  Prerequisites

- [Ollama](https://ollama.com) installed and running locally

###  Install Dependencies and Run!

```bash
pip install -r requirements.txt
```
Run Locally: streamlit run app.py

🙌 Made With Love By
Aarya Shetiye
