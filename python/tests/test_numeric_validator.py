import unittest

from sanio.validators import NumericValidator


class TestNumericValidator(unittest.TestCase):
    def test_trues(self):
        self.assertTrue(NumericValidator.is_float('3.14'))

        self.assertTrue(NumericValidator.is_float(3.14))

        self.assertTrue(NumericValidator.is_integer('1'))

        self.assertTrue(NumericValidator.is_integer(1))

        self.assertTrue(NumericValidator.is_numeric('1'))

        self.assertTrue(NumericValidator.is_numeric(1))

        self.assertTrue(NumericValidator.is_numeric(3.14))

        self.assertTrue(NumericValidator.is_numeric('3.14'))

    def test_falses(self):
        self.assertFalse(NumericValidator.is_integer('TX'))

        self.assertFalse(NumericValidator.is_float('TX'))

        self.assertFalse(NumericValidator.is_float('1'))

        self.assertFalse(NumericValidator.is_float(1))

        self.assertFalse(NumericValidator.is_integer('3.14'))

        self.assertFalse(NumericValidator.is_integer(3.14))

        self.assertFalse(NumericValidator.is_numeric('TX'))

        self.assertFalse(NumericValidator.is_numeric('  TX '))

## ---------------------
if __name__ == "__main__":
    unittest.main()
