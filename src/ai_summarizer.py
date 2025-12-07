import streamlit as st
from transformers import pipeline
from PyPDF2 import PdfReader

st.title("📄 AI Notes + PDF Summarizer")

# Initialize summarization pipeline
@st.cache_resource  # caches the model so it loads only once
def load_model():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_model()

# Upload PDF or paste text
uploaded_file = st.file_uploader("Upload a PDF file (optional)", type="pdf")
text_input = st.text_area("Or paste your text here:")

# Extract text from PDF if uploaded
if uploaded_file:
    from PyPDF2 import PdfReader
    pdf = PdfReader(uploaded_file)
    text_input = ""
    for page in pdf.pages:
        text_input += page.extract_text()

# Summarize button
if st.button("Summarize") and text_input.strip():
    with st.spinner("Summarizing..."):
        # Hugging Face models have a max token limit; we split if too long
        max_chunk = 1000
        chunks = [text_input[i:i+max_chunk] for i in range(0, len(text_input), max_chunk)]
        summary_text = ""
        for chunk in chunks:
            result = summarizer(chunk, max_length=150, min_length=40, do_sample=False)
            summary_text += result[0]['summary_text'] + " "
    st.subheader("Summary:")
    st.write(summary_text)