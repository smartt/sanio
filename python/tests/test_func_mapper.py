import string
import unittest

from sanio.mappers import FuncMapper


class TestFuncMapper(unittest.TestCase):
    #
    # With no mapping function, we echo without changing the type
    #
    def test_a(self):
        fm = FuncMapper()
        self.assertEqual(fm.clean(value=1), 1)

    def test_ab(self):
        fm = FuncMapper()
        self.assertEqual(fm.clean(value='1'), '1')

    def test_b(self):
        fm = FuncMapper()
        self.assertEqual(fm.clean(key='foo', value='bar'), 'bar')

    #
    # Test a simple mapping function
    #
    def test_c(self):
        fm = FuncMapper(fn=int)
        self.assertEqual(fm.clean(key='foo', value='1'), 1)

    #
    # Test a simple mapping function that only maps a specific key
    #
    def test_d(self):
        fm = FuncMapper(fn_map={'bar': int})
        self.assertEqual(fm.clean(key='foo', value='1'), '1')
        self.assertEqual(fm.clean(key='bar', value='1'), 1)

    #
    # Test mapping a list of functions to a key
    #
    def test_e(self):
        fm = FuncMapper(fn_map={'bar': [string.strip, int]})
        self.assertEqual(fm.clean(key='bar', value='   1    '), 1)

    def test_f(self):
        fm = FuncMapper(fn_map={'bar': [string.strip, string.upper]})
        self.assertEqual(fm.clean(key='bar', value='   hi there    '), 'HI THERE')

    def test_g(self):
        fm = FuncMapper(fn_map={'bar': []})
        self.assertEqual(fm.clean(key='bar', value=' woot '), ' woot ')

if __name__ == '__main__':
    unittest.main()
