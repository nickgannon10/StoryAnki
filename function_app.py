import os
import sys
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv

from data_models.questionAnswer import QuestionAnswerPairList
from config.enums import Role, GPTModel, Subject, Age, NumberOfCards # Import the enums

load_dotenv()

AGE = Age.TWENTY_FIVE.value  # Use the enum for age
SUBJECT = Subject.MACHINE_LEARNING.value  # Use the enum for subject
NUMBER_OF_CARDS = NumberOfCards.NUMBER_OF_CARDS.value

sys.path.append(os.getcwd())

prompt_path = os.path.join(os.getcwd(), 'prompts', 'cardGenerator.md')

with open(prompt_path, 'r') as file:
    prompt_template = file.read()

# Format the prompt with AGE and SUBJECT variables
formatted_prompt = prompt_template.format(AGE=AGE, SUBJECT=SUBJECT, NUMBER_OF_CARDS=NUMBER_OF_CARDS)

client = OpenAI()

messages = [
    {"role": Role.SYSTEM.value, "content": "You are a helpful tutor."},  # Using Role enum
    {"role": Role.USER.value, "content": formatted_prompt},
]

completion = client.beta.chat.completions.parse(
    model=GPTModel.GPT_4_2024_AUG.value,  # Using GPTModel enum
    messages=messages,
    response_format=QuestionAnswerPairList,
)

message = completion.choices[0].message
if message.parsed:
    print(message.parsed.QuestionAnswerPairs)
else:
    print(message.refusal)
