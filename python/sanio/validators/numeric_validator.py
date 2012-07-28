from sanio.base import BaseSanio
from sanio.cleaners import StringCleaner


class NumericValidator(BaseSanio):
    @classmethod
    def is_float(cls, s):
        return isinstance(s, (float,))

    @classmethod
    def is_integer(cls, s):
        return isinstance(StringCleaner.safe_int(s), (int,))

    @classmethod
    def is_numeric(cls, s):
        return str(StringCleaner.extract_numbers_safe(s)) == str(s)
