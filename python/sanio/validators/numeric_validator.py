from sanio.base import BaseSanio


class NumericValidator(BaseSanio):
    @classmethod
    def is_float(cls, s):
        return False

    @classmethod
    def is_integer(cls, s):
        return False

    @classmethod
    def is_numeric(cls, s):
        return False
