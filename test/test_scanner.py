import unittest

from yalang.scanner import Scanner
from yalang.token import Token, Type

class TestScan(unittest.TestCase):
    def test_scan_ident(self):
       scanner = Scanner('Hello World!')
       self.assertEqual(scanner.next(), Token('Hello', Type.IDENT))
       self.assertEqual(scanner.next(), Token('World!', Type.IDENT))
       self.assertEqual(scanner.next(), Token(None, Type.EOF))
       self.assertEqual(scanner.next(), Token(None, Type.EOF))

    def test_scan_string(self):
        scanner = Scanner('"Hello World!" ')
        self.assertEqual(scanner.next(), Token('Hello World!', Type.STRING))
        self.assertEqual(scanner.next(), Token(None, Type.EOF))

    def test_scan_ident_utf8(self):
        scanner = Scanner("你好 世界!")
        self.assertEqual(scanner.next(), Token('你好', Type.IDENT))
        self.assertEqual(scanner.next(), Token('世界!', Type.IDENT))
        self.assertEqual(scanner.next(), Token(None, Type.EOF))

    def test_scan_numbers(self):
        scanner = Scanner("39495")
        self.assertEqual(scanner.next(), Token("39495", Type.INT))
        scanner = Scanner("1 + 2 + 10")
        self.assertEqual(scanner.next(), Token("1", Type.INT))
        self.assertEqual(scanner.next(), Token("+", Type.PLUS))
        self.assertEqual(scanner.next(), Token("2", Type.INT))
        self.assertEqual(scanner.next(), Token("+", Type.PLUS))
        self.assertEqual(scanner.next(), Token("10", Type.INT))
