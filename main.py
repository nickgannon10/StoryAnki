import os
import requests
from urllib.parse import urlparse, unquote

from src.services.web_page_processor import WebPagePreprocessor
from src.services.pdf_processor import PDFPreprocessor
from src.services.chunk_processor import ChunkProcessor
from src.utils.openai_client import OpenAIClient

def add_note(deck_name: str, front: str, back: str) -> dict:
    """
    Adds a note to Anki using AnkiConnect.

    :param deck_name: Name of the Anki deck.
    :param front: Front content of the flashcard.
    :param back: Back content of the flashcard.
    :return: Response from AnkiConnect.
    """
    payload = {
        "action": "addNote",
        "version": 6,
        "params": {
            "note": {
                "deckName": deck_name,
                "modelName": "Basic",
                "fields": {
                    "Front": front,
                    "Back": back
                },
                "tags": []
            }
        }
    }
    response = requests.post("http://localhost:8765", json=payload)
    return response.json()

def process_input(input_path: str, output_path: str) -> str:
    """
    Processes the input path based on its type (web page or PDF).

    :param input_path: Path or URL to the input (web page or PDF).
    :param output_path: Path to the directory where the JSON file will be saved.
    :return: Path to the JSON file containing the processed chunks.
    """
    if input_path.startswith("http://") or input_path.startswith("https://"):
        print("Processing web page...")
        preprocessor = WebPagePreprocessor(input_path)
        preprocessor.fetch_content()
        preprocessor.extract_text()
        
        # Write extracted text to markdown for visualization
        preprocessor.write_text_to_markdown(output_path)
        
        print("Please manually edit the extracted_text.md file to remove unnecessary information.")
        input("Press Enter to continue after editing the markdown file...")
        
        # Read the edited text from markdown
        preprocessor.read_text_from_markdown(output_path)
        
        preprocessor.chunk_text(max_tokens=1500)
        preprocessor.write_chunks_to_json(output_path)
        json_file = os.path.join(output_path, "webpage_chunks.json")
    elif input_path.lower().endswith(".pdf"):
        print("Processing PDF...")
        preprocessor = PDFPreprocessor(input_path)
        preprocessor.extract_text()
        
        # Write extracted text to markdown for visualization
        preprocessor.write_text_to_markdown(output_path)
        
        print("Please manually edit the extracted_text.md file to remove unnecessary information.")
        input("Press Enter to continue after editing the markdown file...")
        
        # Read the edited text from markdown
        preprocessor.read_text_from_markdown(output_path)
        
        preprocessor.chunk_text(max_tokens=1500)
        preprocessor.write_chunks_to_json(output_path)
        json_file = os.path.join(output_path, "pdf_chunks.json")
    else:
        raise ValueError("Input must be a valid URL or a PDF file path.")

    print(f"Chunks and token count written to {json_file}")
    return json_file

if __name__ == "__main__":
    # input_path = "/Users/nicholasgannon/sources/repos/autonomous-anki-builder/pdfs/SelfRAG.pdf"
    web_page='https://andymatuschak.org/prompts/'
    output_path = "/Users/nicholasgannon/sources/repos/autonomous-anki-builder/outputs"

    # Process the input based on its type (web page or PDF)
    json_file = process_input(web_page, output_path)

    # Process the first two chunks with OpenAI
    chunk_processor = ChunkProcessor(json_file)
    chunk_processor.process_chunks(num_chunks=2)

    # # Example usage of adding a note to Anki
    # deck_name = "Testing"
    # front = "What is the capital of France?"
    # back = "Paris"
    # result = add_note(deck_name, front, back)
    # print(result)