# Document Summarizer - ChatGPT API using Streamlit

![Project Screenshot](screenshot.png)

## Overview

The **Document Summarizer** is a web application that leverages OpenAI's ChatGPT API to generate concise summaries of documents. Built with Streamlit, this application provides a user-friendly interface for uploading text files, processing them, and obtaining accurate and coherent summaries in just a few clicks.

## Features

- **Upload Document:** Easily upload text files (TXT, PDF) for summarization.
- **Summarization:** Generate a concise summary using the power of the ChatGPT API.
- **Download Summary:** Download the summarized text as a TXT file for future reference.
- **User-friendly Interface:** A simple and clean UI built with Streamlit.
- **Customizable Parameters:** Option to adjust the summarization length and other parameters.

## Installation

### Prerequisites

- Python 3.7 or higher
- An OpenAI API key
- Streamlit

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/Document-Summarizer.git
    cd document-summarizer
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Add your OpenAI API key:

    Create a `.env` file in the root directory of the project and add your API key:

    ```plaintext
    OPENAI_API_KEY=your-api-key-here
    ```

4. Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```

5. Open your browser and navigate to `http://localhost:8501` to use the application.

## Usage

1. **Upload Document:** Click on the "Browse files" button to upload your document.
2. **Summarize:** Click the "Summarize" button to generate a summary.
3. **Download:** Click the "Download Summary" button to save the summary as a TXT file.

## Project Structure

```plaintext
📁 document-summarizer/
├── 📄 document_summarizer_main.py       # Contains the summarization logic using ChatGPT API
├── 📄 requirements.txt    # Python dependencies
└── 📄 README.md           # Project documentation
