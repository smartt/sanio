

class BaseSanio(object):
    def __init__(self, *args, **kwargs):
        self.cleaner = None
        self.filterer = None
        self.data_source = None
        self.verbose = False

        self._reader_generator = None
        self._iter_complete = False

        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __iter__(self):
        return self

    def _clean(self, data):
        """
        Applies your cleaner to your data.
        """
        if isinstance(data, (dict,)):
            out = dict()
        else:
            out = None

        _first = True

        if self.cleaner is not None:
            if not isinstance(self.cleaner, (list,)):
                self.cleaner = list(self.cleaner)

            for obj in self.cleaner:
                try:
                    if isinstance(data, (dict,)):
                        if _first:
                            for k, v in data.items():
                                out[k] = obj.clean(k, v)
                            _first = False

                        else:
                            for k, v in out.items():
                                out[k] = obj.clean(k, v)

                    else:
                        if _first:
                            out = obj.clean(None, data)
                            _first = False

                        else:
                            out = obj.clean(None, out)

                except AttributeError:
                    # self.cleaner is probably None
                    pass

                except TypeError:
                    # self.cleaner.clean isn't callable
                    pass

        if out:
            return out
        else:
            return data

    def _filter(self, data):
        """
        Applies your filterer to your data.
        """
        out = None

        if self.filter is not None:
            # Run the filter on the row
            try:
                out = self.filterer.filter(data)

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
        # This is a dummy cleaning function. It's *not* how you run your cleaner (that's _clean());
        # It's how this object cleans.
        return value

    def filter(self, d):
        # This is a dummy filter function. It's *not* how you run your filters (that's _filter());
        # It's how this object filters.
        return d

    def next(self):
        raise StopIteration
