

class BaseReader(object):
    def __init__(self, *args, **kwargs):
        self._iter_complete = False

        self.cleaner = None
        self.verbose = False

        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __iter__(self):
        return self
