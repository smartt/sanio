

class BaseTransform(object):
    def __init__(self, *args, **kwargs):
        self.cleaner = None
        self.reader = None
        self.verbose = False
        self._reader_generator = None

        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __iter__(self):
        return self
