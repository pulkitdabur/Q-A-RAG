# Q&A RAG-Based Application

## Overview
This application is a Retrieval-Augmented Generation (RAG)-based Q&A system that processes a given input document to generate answers based on user queries. It utilizes a vector database for efficient retrieval and Azure OpenAI for language modeling.

## Features
- Processes the provided input document to generate context-aware responses.
- Stores vector embeddings for efficient retrieval using a vector database.
- Implements a Q&A system using RAG methodology.
- Supports local execution with easy setup.
- Provides test cases to validate functionality.

## Tech Stack
- **Programming Language**: Python
- **Framework**: Streamlit
- **Vector Database**: FAISS DB (rag_qa)
- **LLM Provider**: Azure OpenAI
- **Dependencies**: Specified in `requirements.txt`

## Installation Guide
### Run this application on local:
1. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
2. **Configure Azure OpenAI credentials:**
   - Open `app.py`
   - Update the following details at line **12**:
     - `AzureOpenAI api-key`
     - `AzureOpenAI version`
     - `AzureOpenAI deployment`
     - `AzureOpenAI endpoint`

3. **Add the input file:**
   - Update `app.py` at line **21** to specify the input file (`budget_speech.pdf`).

4. **Run the application:**
   ```sh
   streamlit run run.py
   ```

### Run this application using Docker:
1. **Build the Docker image:**
   ```sh
   docker build -t rag_qa_app .
   ```
2. **Run the application in a container:**
   ```sh
   docker run -p 8501:8501 --env AZURE_OPENAI_API_KEY=your-api-key --env AZURE_OPENAI_VERSION=your-version --env AZURE_OPENAI_DEPLOYMENT=your-deployment --env AZURE_OPENAI_ENDPOINT=your-endpoint rag_qa_app
   ```

## File Structure
- **Input File**: `budget_speech.pdf`
- **Documentation**: `a&A doc.pdf`
- **Vector Database Storage**: `FAISS DB (rag_qa)`
- **Main Application File**: `run.py`
- **RAG Logic File**: `main.py`
- **Test Cases**: `test_Cases.xlsx`

This setup ensures smooth execution of the Q&A application using a structured RAG-based approach.
