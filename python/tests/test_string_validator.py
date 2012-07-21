import unittest

from sanio.validators import StringValidator


class TestStringValidator(unittest.TestCase):
    def test_is_alpha(self):
        self.assertTrue(StringValidator.is_alpha('abc'))
        self.assertTrue(StringValidator.is_alpha('ABC'))

    def test_is_not_alpha(self):
        self.assertFalse(StringValidator.is_alpha('123'))
        self.assertFalse(StringValidator.is_alpha('abc123'))
        self.assertFalse(StringValidator.is_alpha('a1b2c3'))
        self.assertFalse(StringValidator.is_alpha('123ABC'))

    def test_is_empty(self):
        self.assertTrue(StringValidator.is_empty(''))
        self.assertTrue(StringValidator.is_empty('   '))

    def test_is_not_empty(self):
        self.assertFalse(StringValidator.is_empty('TX'))
        self.assertFalse(StringValidator.is_empty('  TX '))

    def test_endswith(self):
        self.assertTrue(StringValidator.endswith('oh hi', 'hi'))

    def test_not_endswith(self):
        self.assertFalse(StringValidator.endswith('hi there', 'hi'))

    def test_startswith(self):
        self.assertTrue(StringValidator.startswith('hi there', 'hi'))

    def test_not_startswith(self):
        self.assertFalse(StringValidator.startswith('oh hi', 'hi'))

## ---------------------
if __name__ == "__main__":
    unittest.main()
