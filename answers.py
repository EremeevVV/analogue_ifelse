from enum import Enum, auto

class Result(Enum):
    NONINT = auto()
    POSITIVE = auto()
    NEGATIVE = auto()
    NULL = auto()
    OVERHUNDRED = auto()

