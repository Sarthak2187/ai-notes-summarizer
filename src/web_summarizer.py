import streamlit as st
from ollama import Client
import PyPDF2

client = Client()

st.title("📄 AI Notes + PDF Summarizer")
st.write("Summarize text or PDFs using your local Llama model.")

# Function to extract text from PDF files
def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

# Input options
uploaded_pdf = st.file_uploader("Upload a PDF file", type=["pdf"])
text_input = st.text_area("Or paste your text here", height=200)

if uploaded_pdf:
    with st.spinner("Extracting text from PDF..."):
        text_input = extract_text_from_pdf(uploaded_pdf)
        st.success("PDF text extracted! You can review or edit the text below:")

# Show extracted text
if text_input:
    st.subheader("Extracted / Input Text")
    st.write(text_input)

# Summarize button
if st.button("Summarize"):
    if not text_input.strip():
        st.error("Please provide text or upload a PDF.")
    else:
        with st.spinner("Summarizing... please wait ⏳"):
            response = client.generate(
                model="llama3.1",
                prompt=f"Summarize this text:\n\n{text_input}"
            )
            summary = response["response"]

        st.subheader("📝 Summary")
        st.write(summary)