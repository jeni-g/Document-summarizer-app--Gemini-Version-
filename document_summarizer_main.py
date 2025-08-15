import os
import re
import string
import docx2txt
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()

# Using Google Gemini to summarize the text
def summarize_text(text):
    prompt = "Summarize the following text. Provide a concise summary based on the input text:\n\n" + text

    # Get the Gemini API key from environment variables
    api_key = os.environ.get("GOOGLE_API_KEY")
    if api_key is None:
        raise ValueError("API key for Google Gemini is not set.")

    # Configure Gemini API
    genai.configure(api_key=api_key)

    # Use Gemini model to generate summary
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    return response.text if hasattr(response, 'text') else "No response from Gemini."


# Create a directory to store uploaded files
def save_uploaded_file(uploaded_file):
    if not os.path.exists("uploads"):
        os.makedirs("uploads")
    with open(os.path.join("uploads", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
    return os.path.join("uploads", uploaded_file.name)


# Process the uploaded file
def process_uploaded_file(uploaded_file):
    content = ""
    if uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        content = docx2txt.process(uploaded_file)
    elif uploaded_file.type == "text/plain":
        content = uploaded_file.read().decode("utf-8")
    return content


# Clean the text
def clean_text(text):
    text = text.lower()
    text = " ".join(text.split())
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)
    text = re.sub(r"[^a-zA-Z0-9\s.]", "", text)
    return text


# Main function
def main():
    st.title('Document Summarizer App (Gemini Version)')
    st.write('Upload a text file or enter text to analyze.')

    uploaded_file = st.file_uploader("Choose a file", type=['txt', 'docx'])
    text_input = st.text_area("Or enter text manually")

    if uploaded_file is not None:
        file_path = save_uploaded_file(uploaded_file)
        content = process_uploaded_file(uploaded_file)
    elif text_input:
        content = text_input.strip()
    else:
        content = None
        st.warning('Please upload a file or enter text.')

    if content and 'content' in locals():
        st.subheader('Original Content')
        st.text_area("Original", value=content, height=400)

        cleaned_content = clean_text(content)
        st.subheader('Preprocessed Content')
        st.text_area("Cleaned", value=cleaned_content, height=400)

        summary = summarize_text(cleaned_content)
        st.subheader('Summary')
        st.text_area("Summarized Text", value=summary, height=300)


if __name__ == "__main__":
    main()
