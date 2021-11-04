from enum import Enum

class MoveType(Enum):
    ILLEGAL_MOVE = 0
    LEGAL_MOVE = 1
    HIT = 2
    BEAR_OFF = 3
    RE_ENTER = 4