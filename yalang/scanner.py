from yalang.token import Token, Type

class Scanner(object):
    def __init__(self, content):
        self.content = content
        self.i = 0

    def next(self):
        if self.i >= len(self.content):
            return self._eof()

        c = self.content[self.i]
        if c == ' ':
            self._incr()
            return self.next()
        elif c == '+':
            plus = self.content[self.i]
            self._incr()
            return Token(plus, Type.PLUS)
        elif c == '"':
            self._incr()
            return self._string()
        elif self._is_digit(c):
            return self._number()
        return self._ident()

    def _eof(self):
        return Token(None, Type.EOF)

    def _incr(self):
        self.i += 1

    def _move(self, stop):
        start = self.i
        while self.i < len(self.content) and self.content[self.i] != stop:
            self._incr()
        return start, self.i

    def _slice(self, start, stop):
        if start >= len(self.content) or stop < start:
            return self._eof()
        return self.content[start:stop]

    def _is_digit(self, c):
        return c.isdigit()

    def _string(self):
        start, stop = self._move('"')
        self._incr()
        return Token(self._slice(start, stop), Type.STRING)

    def _number(self):
        start, stop = self._move(' ')
        self._incr()
        return Token(self._slice(start, stop), Type.INT)

    def _ident(self):
        start, stop = self._move(' ')
        self._incr()
        return Token(self._slice(start, stop), Type.IDENT)
