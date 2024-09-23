import requests

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

def add_notes_to_anki(deck_name: str, qa_list: list) -> None:
    """
    Adds a set of note cards to Anki based on a list of dictionaries with questions and answers.

    :param deck_name: Name of the Anki deck.
    :param qa_list: List of dictionaries containing questions and answers in the format:
                    [{ 'Question': 'What is X?', 'Answer': 'X is ...'}, ... ]
    """
    for idx, qa_dict in enumerate(qa_list):
        question = qa_dict.get('Question')
        answer = qa_dict.get('Answer')

        if question and answer:
            result = add_note(deck_name, question, answer)
            print(f"Added card {idx+1}: {result}")
        else:
            print(f"Skipped card {idx+1} (missing Question or Answer)")

if __name__ == "__main__":
    # Example list of questions and answers
    qa_list = [
        {'Question': 'What is the final stage of AlphaFold known as?', 
        'Answer': 'The final stage of AlphaFold is called EVOFormer. The Evoformer in AlphaFold is a neural network module that processes evolutionary (Multiple Sequence Alignment) and pairwise amino acid relationships to extract structural information and predict protein folding. It uses self-attention mechanisms and communication blocks to refine these representations, playing a crucial role in AlphaFold’s ability to accurately predict 3D protein structures.'},
        
        {'Question': 'What is DiffDock, and what method does it use for ligand docking?', 
        'Answer': 'DiffDock is a diffusion model used for ligand docking, and it employs a method called confidence bootstrapping, similar to MCT (Monte Carlo Tree Search).'},

        {'Question': 'What is RoseTTAFold All-Atom (RFAA) used for?', 
        'Answer': 'RoseTTAFold All-Atom (RFAA) is used for modeling complexes involving proteins and small molecules, DNA, RNA, or metals.'},

        {'Question': 'How does RFdiffusion All-Atom (RFdiffusionAA) extend RoseTTAFold All-Atom?', 
        'Answer': 'RFdiffusion All-Atom (RFdiffusionAA) extends RFAA by building protein structures around small molecules.'},

        {'Question': 'What is ProteinDT, and how does it function?', 
        'Answer': 'ProteinDT is a multi-modal framework designed for protein design tasks, using both textual descriptions and protein sequence information.'}
    ]


    # Specify the Anki deck name
    deck_name = "A Little Bit of Everything"

    # Add the cards to Anki
    add_notes_to_anki(deck_name, qa_list)
    print("should be complete")
