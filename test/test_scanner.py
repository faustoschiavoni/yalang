import unittest

from yalang import scanner

class TestScan(unittest.TestCase):
    def test_scan(self):
        scanner.scan()
        self.assertEqual(1, 1)
