from enum import Enum


class Role(Enum):
    SYSTEM = "system"
    USER = "user"

class GPTModel(Enum):
    GPT_4_2024_AUG = "gpt-4o-2024-08-06"
    # Add other models here as needed


class Subject(Enum):
    MACHINE_LEARNING = "Machine Learning"
    # Add other subjects here as needed


class Age(Enum):
    TWENTY_FIVE = 25
    # Add other age values here if needed

class NumberOfCards(Enum):
    NUMBER_OF_CARDS = 10


class ResponseStatus(Enum):
    SUCCESS = "Success"
    FAILURE = "Failure"
    # You can add more response statuses based on how you handle completions
