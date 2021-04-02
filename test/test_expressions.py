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


class TestStream(unittest.TestCase):
    def test_stream_in(self):
        self.assertEqual(exec_ok('''
            f = <in> (n) {
                return n + << in;
            };
            1 >> f<in>;
            f(18)
        '''), '19')

    def test_stream_out(self):
        self.assertEqual(exec_ok('''
            f = (s) <out> {
                s >> out;
            };
            f('hello');
            << f<out>
        '''), "'hello'")

    def test_connect_fns(self):
        self.assertEqual(exec_ok('''
            f = (n) <out> {
                n + 1 >> out;
            };
            g = () <out> {
                << f<out> + 1 >> out;
            };
            f(1);
            g();
            << g<out>
        '''), '3')

    def test_name_clash(self):
        self.assertEqual(exec_ko('''
            f = <a> () <a> { 1; }
        '''), "line 2:16 Name clash between input and output streams")

    def test_read_too_much(self):
        self.assertEqual(exec_ko('''
            f = (s) <out> {
                s >> out;
            };
            f('hello');
            << f<out>;
            << f<out>
        '''), "line 7:12 Attempted read from empty stream")

    def test_read_illegal_rw(self):
        self.assertEqual(exec_ko('''
            f = <in> () <out> {
                << out;
            };
            f()
        '''), "line 3:16 Cannot read from output within function")
        self.assertEqual(exec_ko('''
            f = <in> () <out> {
                1 >> in;
            };
            f()
        '''), "line 3:16 Cannot write to input within function")
        self.assertEqual(exec_ko('''
            f = <in> () <out> {
                1 >> out;
            };
            1 >> f<out>
        '''), "line 5:12 Cannot write to output of another function")
        self.assertEqual(exec_ko('''
            f = <in> () <out> {
                1 >> out;
            };
            << f<in>
        '''), "line 5:12 Cannot read from input to another function")

    def test_nested(self):
        self.assertEqual(exec_ok('''
            f = <in> (n) <out> {
                g = <in> (n) <out> {
                    << in * n >> out;
                };
                << in + n >> g<in>;
                g(n + 1);
                << g<out> >> out;
            };
            2 >> f<in>;
            f(0.5);
            << f<out>
        '''), '3.75')
        self.assertEqual(exec_ko('''
            f = <in> (n) <out> {
                g = <in> (n) <out> {
                    1 >> out;
                    1 >> in;
                };
                g(n + 1);
            };
            f(1)
        '''), "line 5:20 Cannot write to input within function")
        self.assertEqual(exec_ko('''
            f = <in> (n) <out> {
                g = <in> (n) <out> {
                    1 >> out;
                    << out;
                };
                g(n + 1);
            };
            f(1)
        '''), "line 5:20 Cannot read from output within function")
