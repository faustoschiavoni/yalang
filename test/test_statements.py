import unittest

from test.utils import *

class TestStatements(unittest.TestCase):
    def test_return(self):
        self.assertEqual(exec_ko('''
            b = a + 1;
            return b
        '''), 'line 3:12 Return statement is allowed only in functions')
