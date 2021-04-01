import unittest

from test.utils import *

class TestMath(unittest.TestCase):
    def test_simple_math(self):
        self.assertEqual(exec_ok("5 + 5"), '10')
        self.assertEqual(exec_ok("5 + -5"), '0')
        self.assertEqual(exec_ok("5 + 1 * 3"), '8')
        self.assertEqual(exec_ok("(5 + 1) * 3"), '18')
        self.assertEqual(exec_ko("5 + 'hello'"), "line 1:0 Binary Math on non-numeric values: 5 + 'hello'")
        self.assertEqual(exec_ok("5.01 + 3.1"), '8.11')
        self.assertEqual(exec_ok("11 + 1.9"), '12.9')


class TestAssignIdent(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(exec_ok("a = 3"), '3')
        self.assertEqual(exec_ok("a = 3 + 3 * 10"), '33')
        self.assertEqual(exec_ok("a = (3 + 3) * 10"), '60')
        self.assertEqual(exec_ok("a = 'hello'"), "'hello'")
        self.assertEqual(exec_ok("a = 3"), '3')

        self.assertEqual(exec_ok("a = 3; a + 4"), '7')
        self.assertEqual(exec_ok("a = b = 3; a + b"), '6')
