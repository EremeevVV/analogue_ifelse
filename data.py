from enum import Enum, auto
from dataclasses import dataclass


@dataclass
class InputData:
    digit: int
    text: str


class ResultData(Enum):
    NONINT = auto()
    POSITIVE = auto()
    NEGATIVE = auto()
    NULL = auto()
    OVERHUNDRED = auto()
    POSITIVE_STRING1 = auto()
    OVERHUNDRED_STRING2 = auto()


