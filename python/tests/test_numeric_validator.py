import unittest

from sanio.validators import NumericValidator


class TestNumericValidator(unittest.TestCase):
    def test_a(self):
        self.assertTrue(NumericValidator.is_float('3.14'))

    def test_b(self):
        self.assertTrue(NumericValidator.is_float(3.14))

    def test_c(self):
        self.assertTrue(NumericValidator.is_integer('1'))

    def test_d(self):
        self.assertTrue(NumericValidator.is_integer(1))

    def test_e(self):
        self.assertTrue(NumericValidator.is_numeric('1'))

    def test_f(self):
        self.assertTrue(NumericValidator.is_numeric(1))

    def test_g(self):
        self.assertTrue(NumericValidator.is_numeric(3.14))

    def test_h(self):
        self.assertTrue(NumericValidator.is_numeric('3.14'))

    def test_i(self):
        self.assertFalse(NumericValidator.is_integer('TX'))

    def test_j(self):
        self.assertFalse(NumericValidator.is_float('TX'))

    def test_k(self):
        self.assertFalse(NumericValidator.is_float('1'))

    def test_l(self):
        self.assertFalse(NumericValidator.is_float(1))

    def test_m(self):
        self.assertFalse(NumericValidator.is_integer('3.14'))

    def test_n(self):
        self.assertFalse(NumericValidator.is_integer(3.14))

    def test_o(self):
        self.assertFalse(NumericValidator.is_numeric('TX'))

    def test_p(self):
        self.assertFalse(NumericValidator.is_numeric('  TX '))

## ---------------------
if __name__ == "__main__":
    unittest.main()
