import enum

class Token(object):
    def __init__(self, content, type):#costruttori detti anche "ctor"
        self.content = content
        self.type = t

class Type(enum.Enum):
    INT = 1
    IDENT = 2
    STRING = 3
    PLUS = 4