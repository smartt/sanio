import unittest

from sanio.cleaners import StringCleaner
from sanio.mappers import FuncMapper
from sanio.readers import StringReader


class TestStringReader(unittest.TestCase):
    def test_simple(self):
        sr = StringReader('hello world')

        self.assertEqual(str(sr), 'hello world')

        self.assertEqual(sr, 'hello world')

        self.assertEqual([i for i in sr], ['hello world'])

    def test_string_of_numbers(self):
        sr = StringReader('123456')

        self.assertEqual(sr, '123456')

        self.assertEqual([i for i in sr], ['123456'])

    def test_cast_string_of_numbers(self):
        sr = StringReader('123456', cleaner=FuncMapper(StringCleaner.safe_int))

        # This one is cheaky, since repr() always returns a string
        self.assertEqual(sr, '123456')

        self.assertEqual([i for i in sr], [123456])

    def test_string_mapper(self):
        sr = StringReader('hello world', cleaner=FuncMapper(StringCleaner.super_flat))
        self.assertEqual(sr, 'HELLOWORLD')

        self.assertEqual([i for i in sr], ['HELLOWORLD'])


## ---------------------
if __name__ == "__main__":
    unittest.main()
