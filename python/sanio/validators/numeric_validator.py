from sanio.base_sanio import BaseSanio


class NumericValidator(BaseSanio):
    def __init__(self, *args, **kwargs):
        super(NumericValidator, self).__init__(*args, **kwargs)

    @classmethod
    def is_float(cls, s):
        return False

    @classmethod
    def is_integer(cls, s):
        return False

    @classmethod
    def is_numeric(cls, s):
        return False
