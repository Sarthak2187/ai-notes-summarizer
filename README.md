# ai-notes-summarizer
A lightweight local AI notes and PDF summarizer built using Python, Streamlit, and Ollama (Llama 3.1).

📘 AI Notes + PDF Summarizer

A lightweight, private, fully offline AI summarizer built using Python, Streamlit, and Llama 3.1 via Ollama.

🚀 Overview

AI Notes + PDF Summarizer is a simple but powerful local AI tool that can:

📝 Summarize long text

📄 Extract and summarize PDF files

🌐 Run entirely offline using Llama 3.1 (via Ollama)

⚡ Provide fast, clean summaries through a modern web UI

🔒 Ensure 100% privacy — your data never leaves your machine

Built in just a few hours as a fun experiment with local LLMs.

🛠 Tech Stack

Python 3

Streamlit — lightweight web UI

Ollama — local LLM engine

Llama 3.1 — summarization model

PyPDF2 — PDF text extraction

📦 Installation
1. Clone the repo
git clone https://github.com/<your-username>/ai-notes-summarizer.git
cd ai-notes-summarizer

2. Install dependencies
pip3 install -r requirements.txt

3. Install & pull the model (if not done already)

Install Ollama:
https://ollama.com/download

Pull the Llama 3.1 model:

ollama pull llama3.1

▶️ Run the app

Use Streamlit to launch the web UI:

streamlit run src/web_summarizer.py


Then open the app at:

http://localhost:8501

🧠 Features
✅ Text Summarization

Paste any text and generate a clean summary.

📄 PDF Summarization

Upload a PDF — the app extracts text automatically.

🔒 Fully Local

No cloud APIs. Nothing leaves your machine.

⚙️ Extendable

Easy to add support for:

DOCX summarization

URL summarization

OCR for images

Audio-to-text summarization

📁 Project Structure
ai-notes-summarizer/
│── src/
│   └── web_summarizer.py   # Main Streamlit app
│── requirements.txt
│── README.md
│── .gitignore

Pull requests are welcome!
