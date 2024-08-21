from dataclasses import dataclass
from random import choice


@dataclass
class Quote:
    text: str
    author: str


quote_list = [
    Quote(text="60% of the time, it works every time.", author="Brian Fantana"),
    Quote(text="All models are wrong, but some are useful.", author="George E. P. Box"),
    Quote(
        text="If you torture the data long enough, it will confess.",
        author="Ronald Coase",
    ),
    Quote(
        text="The hardest thing in machine learning is debugging the model.",
        author="Geoffrey Hinton",
    ),
]


def get_random_quote() -> Quote:
    return choice(quote_list)
