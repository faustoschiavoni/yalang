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


class TestFn(unittest.TestCase):
    def test_fn_simple(self):
        self.assertEqual(exec_ok('''
            f = (n) {
                return n + 1;
            };
            f(18)
        '''), '19')

    def test_fn_multiple_invocation(self):
        self.assertEqual(exec_ok('''
            a = 3;
            f = (n) {
                a = a + 1;
                return n + a;
            };
            f(18);
            f(18)
        '''), '22')

    def test_scope_shadowing(self):
        self.assertEqual(exec_ok('''
            a = 5;
            f = (n) {
                a = 3;
                return a + n;
            };
            f(a)
        '''), '8')
        self.assertEqual(exec_ok('''
            a = 5;
            f = (n) {
                return a + n;
            };
            f(a)
        '''), '10')
        self.assertEqual(exec_ok('''
            a = 5;
            f = (n) {
                a = 3;
                return a + n;
            };
            b = f(a);
            a
        '''), '5')

    def test_multi_arity(self):
        self.assertEqual(exec_ok('''
            a = 5;
            f = (a, b, c) {
                d = 2;
                return (a + b + c) * d;
            };
            f(a, 2, 3)
        '''), '20')
        self.assertEqual(exec_ko('''
            a = 5;
            f = (a, b, c) {
                d = 2;
                return (a + b + c) * d;
            };
            f(a, 2)
        '''), 'line 7:12 function requires 3 args, 2 given')

    def test_dead_code(self):
        self.assertEqual(exec_ok('''
            f = (a, b) {
                return a * b;
                d = 2;
                return error_here;
            };
            f(3 + 1.2, 2 * 10)
        '''), '84.0')

    def test_error_in_fn(self):
        self.assertEqual(exec_ko('''
            f = (a, b) {
                return a + b;
            };
            f(1, 'hello')
        '''), "line 3:23 Binary Math on non-numeric values: 1 + 'hello'")

    def test_nested(self):
        self.assertEqual(exec_ok('''
            n = 3;
            f = (a, b) {
                n = 1;
                g = (n) {
                    return n + 1;
                };
                return a + g(b) + n;
            };
            f(n, 4)
        '''), '9')
        self.assertEqual(exec_ko('''
            n = 3;
            f = (a, b) {
                n = 1;
                g = (n) {
                    return 'n' + 1;
                };
                return a + g(b) + n;
            };
            f(n, 4)
        '''), "line 6:27 Binary Math on non-numeric values: 'n' + 1")

    def test_nested_fn_shadowing(self):
        self.assertEqual(exec_ok('''
            n = 3;
            f = (a, b) {
                n = 1;
                f = (n) {
                    return n + 1;
                };
                return a + f(b) + n;
            };
            f(n, 4)
        '''), '9')

    def test_closure(self):
        self.assertEqual(exec_ok('''
            n = 3;
            f = (a, b) {
                return a - b - n;
            };
            n = 4;
            f(1, 2)
        '''), '-4')

    def test_not_callable(self):
        self.assertEqual(exec_ko('''
            n = 3;
            n(1)
        '''), "line 3:12 variable is not callable")
