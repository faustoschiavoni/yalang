import unittest

from test.utils import *

class TestStatements(unittest.TestCase):
    def test_return(self):
        self.assertEqual(exec_ko('''
            b = 1 + 1;
            return b
        '''), 'line 3:12 Return statement is allowed only in functions')
