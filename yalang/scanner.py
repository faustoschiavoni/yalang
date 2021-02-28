from yalang.token import Token, Type

class Scanner(object):
    def __init__(self, content):
        self.content = content
        self.i = 0

    def next(self):
        if self.i >= len(self.content):
            return None
        start = self.i
        while self.i < len(self.content) and self.content[self.i] != ' ':
            self.i += 1
        self.i += 1
        return self.content[start:self.i-1]
