import os, logging, json
from typing import List, Dict
from src.utils.openai_client import OpenAIClient

class ChunkProcessor:
    def __init__(self, json_file: str):
        """
        Initializes the ChunkProcessor with the given JSON file path.

        :param json_file: Path to the JSON file containing the processed chunks.
        """
        self.json_file = json_file
        self.chunks = self._load_chunks()
        self.prompt_template = self._load_prompt_template()

    def _load_chunks(self) -> List[str]:
        """
        Loads chunks from the JSON file.

        :return: List of chunks.
        """
        with open(self.json_file, "r") as f:
            data = json.load(f)
            chunks = data.get("chunks", [])
            return chunks

    def _load_prompt_template(self) -> str:
        """
        Loads the prompt template from the markdown file.

        :return: Prompt template as a string.
        """
        current_dir = os.path.dirname(os.path.abspath(__file__))
        prompt_path = os.path.join(current_dir, '..', 'prompts', 'chunk_to_notecard.md')

        with open(prompt_path, "r") as file:
            prompt_template = file.read()
        return prompt_template

    def process_chunks(self, num_chunks: int = 2) -> List[Dict]:
        """
        Processes the specified number of chunks using the OpenAI client.

        :param num_chunks: Number of chunks to process.
        :return: List of responses from the OpenAI client.
        """
        if not self.chunks:
            print("No chunks found in the JSON file.")
            return []

        openai_client = OpenAIClient()
        responses = []

        for i, chunk in enumerate(self.chunks[:num_chunks]):
            # Escape the text content to handle quotes properly
            escaped_chunk = json.dumps(chunk)
            prompt = self.prompt_template.replace("{TEXT_CONTENT}", escaped_chunk)
            messages = [{"role": "system", "content": "You are a helpful assistant designed to output JSON."},
                        {"role": "user", "content": prompt}]
            response = openai_client.generate_completion(messages=messages)
            
            if response.choices[0].finish_reason == "stop":
                try:
                    json_response = json.loads(response.choices[0].message.content)
                    responses.append(json_response)
                except json.JSONDecodeError as e:
                    logging.error(f"JSON decode error: {e}")
                    responses.append({"error": "Failed to parse JSON response"})
            else:
                responses.append({"error": "Response not completed successfully"})

            print(f"Chunk {i+1} response: {response}")

        return responses