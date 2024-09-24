from pydantic import BaseModel

class QuestionAnswerPair(BaseModel):
    Question: str
    Answer: str


class QuestionAnswerPairList(BaseModel):
    QuestionAnswerPairs: list[QuestionAnswerPair]