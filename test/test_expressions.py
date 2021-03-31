import unittest

from yalang import execute_string, YalangException

class TestMath(unittest.TestCase):
    def exec(self, stmt):
        v = execute_string(stmt + ';', debug=True)
        if v is not None and len(v.debug_info) > 0:
            return v.debug_info[-1].value
        return None

    def exec_error(self, stmt):
        try:
            v = execute_string(stmt + ';', debug=True)
            print(v.debug_info)
            return None
        except YalangException as e:
            return str(e)

    def test_simple_math(self):
        self.assertEqual(self.exec("5 + 5"), '10')
        self.assertEqual(self.exec("5 + -5"), '0')
        self.assertEqual(self.exec("5 + 1 * 3"), '8')
        self.assertEqual(self.exec("(5 + 1) * 3"), '18')
        self.assertEqual(self.exec_error("5 + hello"), 'Binary Math on non-numeric values: 5 + hello')
        self.assertEqual(self.exec("5.01 + 3.1"), '8.11')
        self.assertEqual(self.exec("11 + 1.9"), '12.9')