import os
import concurrent.futures
from pdf_processor import process_pdf
from mongodb_handler import MongoDBHandler
import json


def load_json_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def main():
    # Load the JSON containing the PDF URLs
    json_data = load_json_data(r'D:\Wasserstoff Project\Dataset\Dataset.json')

    # Initialize MongoDB handler
    db_handler = MongoDBHandler()

    # Folder to store downloaded PDFs
    pdf_folder = r"D:\Wasserstoff Project\pdfs"
    os.makedirs(pdf_folder, exist_ok=True)

    # Process each PDF in parallel using concurrency
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for pdf_key, pdf_url in json_data.items():
            pdf_path = os.path.join(pdf_folder, f"{pdf_key}.pdf")
            futures.append(executor.submit(process_pdf, pdf_url, pdf_path, db_handler))

        # Wait for all threads to complete
        for future in concurrent.futures.as_completed(futures):
            print(future.result())


if __name__ == "__main__":
    main()
