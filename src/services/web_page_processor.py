import requests
from bs4 import BeautifulSoup
import tiktoken
import json
import os
from typing import List

class WebPagePreprocessor:
    def __init__(self, url: str):
        """
        Initializes the WebPagePreprocessor with the given URL.

        :param url: URL of the web page to preprocess.
        """
        self.url = url
        self.html_content: str = ""
        self.text_content: str = ""
        self.chunks: List[str] = []
        self.total_tokens: int = 0

    def fetch_content(self) -> None:
        """
        Fetches the HTML content from the web page.
        """
        response = requests.get(self.url)
        if response.status_code == 200:
            self.html_content = response.text
        else:
            raise Exception(f"Failed to fetch web page. Status code: {response.status_code}")

    def extract_text(self) -> None:
        """
        Extracts text content from the HTML content of the web page.
        """
        if not self.html_content:
            raise Exception("HTML content is empty. Fetch content first.")
        
        soup = BeautifulSoup(self.html_content, 'html.parser')
        
        paragraphs = soup.find_all('p')
        self.text_content = "\n".join([para.get_text() for para in paragraphs])

    def write_text_to_markdown(self, output_path: str) -> None:
        """
        Writes the extracted text content to a markdown file in the specified output directory.

        :param output_path: Path to the directory where the markdown file will be saved.
        """
        if not self.text_content:
            raise Exception("Text content is empty. Extract text first.")
        
        output_file = os.path.join(output_path, "extracted_text.md")
        with open(output_file, "w") as f:
            f.write(self.text_content)

    def read_text_from_markdown(self, input_path: str) -> None:
        """
        Reads the text content from a markdown file.

        :param input_path: Path to the markdown file containing the edited text.
        """
        input_file = os.path.join(input_path, "extracted_text.md")
        if not os.path.exists(input_file):
            raise Exception("Markdown file does not exist. Please provide a valid path.")
        
        with open(input_file, "r") as f:
            self.text_content = f.read()

    def chunk_text(self, max_tokens: int = 1500) -> None:
        """
        Chunks the text content into increments of specified maximum tokens.

        :param max_tokens: Maximum number of tokens per chunk.
        """
        if not self.text_content:
            raise Exception("Text content is empty. Extract text first.")
        
        tokenizer = tiktoken.get_encoding("cl100k_base")
        tokens = tokenizer.encode(self.text_content)
        self.total_tokens = len(tokens)  # Counting total tokens
        
        self.chunks = [tokens[i:i + max_tokens] for i in range(0, len(tokens), max_tokens)]
        self.chunks = [tokenizer.decode(chunk) for chunk in self.chunks]

    def write_chunks_to_json(self, output_path: str) -> None:
        """
        Writes the chunks to a JSON file in the specified output directory.

        :param output_path: Path to the directory where the JSON file will be saved.
        """
        if not self.chunks:
            raise Exception("Chunks are empty. Chunk text first.")
        
        output_file = os.path.join(output_path, "webpage_chunks.json")
        with open(output_file, "w") as f:
            json.dump({
                "total_tokens": self.total_tokens,
                "chunks": self.chunks
            }, f, indent=4)

    def get_text_content(self) -> str:
        """
        Returns the extracted text content.

        :return: The extracted text content.
        """
        return self.text_content
