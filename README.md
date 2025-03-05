# PDF Summarizer and Chatbot

A Gradio-based web application that allows users to upload PDF files for summarization and interact with a chatbot.

## Features

- PDF file upload and summarization
- Chatbot interface for questions about the content
- Simple and intuitive user interface
- Powered by LLaMA 3.1 model through Ollama

## Prerequisites

- Python 3.10+
- Ollama with LLaMA 3.1 model installed
- Required Python libraries (see Installation)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/rohithgg/pdf-summarizer-chatbot.git
   cd pdf-summarizer-chatbot
   ```

2. Install the required dependencies:
   ```
   pip install -r requirement.txt
   ```

3. Make sure you have Ollama installed with the LLaMA 3.1 model:
   ```
   ollama pull llama3.1
   ```

## Usage

1. Run the application:
   ```
   python gradio-ui.py
   ```

2. Open your browser and navigate to the URL displayed in the terminal (usually http://127.0.0.1:7860)

3. Using the PDF Summarizer:
   - Select the "PDF Summarizer" tab
   - Upload a PDF file using the file uploader
   - Wait for the summarization process to complete
   - Read the summary displayed in the text box

4. Using the Chatbot:
   - Select the "Chatbot" tab
   - Type your question in the input box
   - Click the submit button to get a response

5. To share the application temporarily, use the URL displayed in the terminal that starts with "https://".

## How It Works

The application uses:
- `pdfplumber` to extract text from PDF files
- `langchain-ollama` to interact with the LLaMA 3.1 model
- `langgraph` to create a workflow for the chatbot
- `gradio` to create the web interface
![image](https://github.com/user-attachments/assets/862509c0-0898-4981-b66c-1cbaabd3f984)


## Notes

- The quality of summarization depends on the model used
- Processing large PDF files may take a while
- The temporary public URLs for sharing expire after a limited time

## Author

Rohith Gona ([rohithgg](https://rohithgg.github.io/rohithsresume))
