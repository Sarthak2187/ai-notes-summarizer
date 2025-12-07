📘 AI Notes + PDF Summarizer

A lightweight, private, fully offline AI summarizer built using Python, Streamlit, and Transformers.

🚀 Overview

AI Notes + PDF Summarizer is a simple but powerful local AI tool that can:

📝 Summarize long text

📄 Extract and summarize PDF files

🌐 Run online using Streamlit

⚡ Provide fast, clean summaries through a modern web UI

Built in just a few hours as a fun experiment with LLM

🛠 Tech Stack

Python 3

Streamlit — lightweight web UI

Transformers - LLM model

PyPDF2 — PDF text extraction

📦 Installation
1. Clone the repo
git clone https://github.com/<your-username>/ai-notes-summarizer.git
cd ai-notes-summarizer

2. Install dependencies
pip3 install -r requirements.txt

3. Install & pull the model (if not done already)
   
▶️ Run the app

Use Streamlit to launch the web UI:

streamlit run src/ai_summarizer.py


Then open the app at:

http://localhost:8501

🧠 Features
✅ Text Summarization

Paste any text and generate a clean summary.

📄 PDF Summarization

Upload a PDF — the app extracts text automatically.

⚙️ Extendable

Easy to add support for:

DOCX summarization

URL summarization

OCR for images

Audio-to-text summarization

📁 Project Structure
ai-notes-summarizer/
│── src/
│   └── ai_summarizer.py   # Main Streamlit app
│── requirements.txt
│── README.md
│── .gitignore

Pull requests are welcome!
