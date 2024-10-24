# PDF Summarization and Keyword Extraction Pipeline

## Overview

This project implements a dynamic pipeline for processing multiple PDF documents, generating domain-specific summaries, extracting keywords, and storing the results in a MongoDB database. The pipeline is designed to handle documents of various lengths, from short to long, and prioritize performance and concurrency.

## Features

- **Concurrent PDF Processing**: Handles multiple PDFs in parallel to optimize performance.
- **Summarization**: Provides concise summaries for short documents and detailed summaries for longer documents.
- **Keyword Extraction**: Extracts domain-specific keywords, excluding generic or irrelevant terms.
- **MongoDB Integration**: Stores PDF metadata, summaries, and keywords in a MongoDB collection.

## Requirements

### Software
- Python 3.x
- MongoDB (running on localhost)

### Python Libraries
Install the required libraries using `pip`:
```bash
pip install pymongo requests pdfminer.six nltk
