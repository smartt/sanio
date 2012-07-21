from sanio.base_sanio import BaseSanio


class StringValidator(BaseSanio):
    def __init__(self, *args, **kwargs):
        super(StringValidator, self).__init__(*args, **kwargs)

    @classmethod
    def startswith(cls, s, key):
        return s.startswith(key)

    @classmethod
    def endswith(cls, s, key):
        return s.endswith(key)

    @classmethod
    def contains(cls, s, key):
        return s.find(key) >= 0

    @classmethod
    def is_alpha(cls, s):
        return False

    @classmethod
    def is_empty(cls, s):
        return False
