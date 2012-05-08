

class BaseParser(object):
    def __init__(self, *args, **kwargs):
        self.cleaner = None
        self.reader = None
        self.verbose = False

        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __iter__(self):
        return self
