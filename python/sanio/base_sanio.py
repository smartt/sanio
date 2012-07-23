

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

    def _clean(self, data):
        out = None

        if self.cleaner is not None:
            try:
                if isinstance(data, (dict,)):
                    for k, v in data.items():
                        out[k] = self.cleaner.clean(k, v)

                else:
                    out = self.cleaner.clean(None, data)

            except AttributeError:
                # self.cleaner is probably None
                pass

            except TypeError:
                # self.cleaner.clean isn't callable
                pass

        if out is not None:
            return out
        else:
            return data

    def _filter(self, data):
        out = None

        if self.filter is not None:
            # Run the filter on the row
            try:
                out = self.filter.filter(data)

            except AttributeError:
                # self.filter is probably None
                pass

            except TypeError:
                # self.filter.filter isn't callable
                pass

        if out is not None:
            return out
        else:
            return data

    def clean(self, key=None, value=None):
        return value

    def filter(self, d):
        return d

    def next(self):
        raise StopIteration
