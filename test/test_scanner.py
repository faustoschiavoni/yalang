import unittest

from yalang.scanner import Scanner

class TestScan(unittest.TestCase):
    def test_scan(self):
       scanner = Scanner('Hello World!')
       self.assertEqual(scanner.next(),'Hello')
       self.assertEqual(scanner.next(),'World!')
       self.assertEqual(scanner.next(), None)
       self.assertEqual(scanner.next(), None)
       self.assertEqual(scanner.next(), None)
       self.assertEqual(scanner.next(), None)

    def test_scan_utf8(self):
        scanner = Scanner("你好 世界!")
        self.assertEqual(scanner.next(),'你好')
        self.assertEqual(scanner.next(),'世界!')
        self.assertEqual(scanner.next(), None)

    def test_scan_numbers(self):
        scanner = Scanner("39495")
        self.assertEqual(scanner.next(),"39495")
