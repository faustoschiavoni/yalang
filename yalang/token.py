import enum

class Token(object):
    def __init__(self, content, t):#costruttori detti anche "ctor"
        self.content = content
        self.type = t

    def __repr__(self):
        return '{} - \'{}\''.format(self.type.name, self.content)

    def __eq__(self, other):
        return type(self) == type(other) and \
            self.content == other.content and \
            self.type == other.type

class Type(enum.Enum):
    EOF = 0

    INT = 1
    IDENT = 2
    STRING = 3
    PLUS = 4
