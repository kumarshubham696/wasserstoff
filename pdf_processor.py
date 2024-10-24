import requests
import os
import logging
from pdfminer.high_level import extract_text
from summarization import summarize_text, extract_keywords
from mongodb_handler import MongoDBHandler


def download_pdf(url, pdf_path):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(pdf_path, 'wb') as f:
            f.write(response.content)
        return True
    except requests.exceptions.RequestException as e:
        logging.error(f"Error downloading {url}: {e}")
        return False


def process_pdf(url, pdf_path, db_handler: MongoDBHandler):
    if not download_pdf(url, pdf_path):
        return f"Failed to download PDF: {url}"

    try:
        # Extract text from the PDF
        text = extract_text(pdf_path)

        if not text.strip():
            raise ValueError(f"No text extracted from {pdf_path}")

        # Generate summary and keywords
        summary = summarize_text(text)
        keywords = extract_keywords(text)

        # Store in MongoDB
        document_metadata = {
            "pdf_url": url,
            "pdf_path": pdf_path,
            "summary": summary,
            "keywords": keywords,
        }
        db_handler.update_document(url, document_metadata)

        return f"Processed and updated MongoDB for: {pdf_path}"
    except Exception as e:
        logging.error(f"Error processing {pdf_path}: {e}")
        return f"Error processing {pdf_path}: {e}"
