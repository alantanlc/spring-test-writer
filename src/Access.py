from enum import Enum, auto

class Access(Enum):
    PRIVATE = auto()
    DEFAULT = auto()
    PROTECTED = auto()
    PUBLIC = auto()