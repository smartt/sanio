from sanio.base import BaseSanio


class StringValidator(BaseSanio):
    def __init__(self, *args, **kwargs):
        super(StringValidator, self).__init__(*args, **kwargs)

    @classmethod
    def contains(cls, s, key):
        return s.find(key) >= 0

    @classmethod
    def count(cls, s, key):
        return s.count(key)

    @classmethod
    def endswith(cls, s, key):
        return s.endswith(key)

    @classmethod
    def find(cls, s, key):
        return s.find(key)

    @classmethod
    def is_alpha(cls, s):
        return False

    @classmethod
    def is_empty(cls, s):
        return False

    @classmethod
    def index(cls, s, key):
        return s.index(key)

    @classmethod
    def rfind(cls, s, key):
        return s.rfind(key)

    @classmethod
    def startswith(cls, s, key):
        return s.startswith(key)
