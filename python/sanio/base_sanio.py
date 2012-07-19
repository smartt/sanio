

class BaseSanio(object):
    def __init__(self, *args, **kwargs):
        self.cleaner = None
        self.filter = None
        self.data_source = None
        self.verbose = False

        self._iter_complete = False

        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __iter__(self):
        return self

    def _clean(self, line):
        if self.cleaner is not None:
            try:
                line = self.cleaner.clean(None, line)

            except AttributeError:
                # self.cleaner is probably None
                pass

            except TypeError:
                # self.cleaner.clean isn't callable
                pass

        return line

    def clean(self, key=None, value=None):
        return value

    def filter(self, d):
        return d

    def next(self):
        raise StopIteration
