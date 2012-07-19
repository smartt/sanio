from sanio.base_sanio import BaseSanio


class ListReader(BaseSanio):
    def __init__(self, data, *args, **kwargs):
        self.original_data = data
        self.data = self.seek(0)
        self._index = 0

        super(ListReader, self).__init__(*args, **kwargs)

    def __str__(self):
        return self.data

    def __unicode__(self):
        return self.data

    def __repr__(self):
        result = None

        if self.cleaner is not None:
            try:
                result = "'{s}'".format(s=self.cleaner.clean(None, self.data))

            except AttributeError:
                # self.cleaner is probably None
                result = "'{s}'".format(s=self.data)

            except TypeError:
                # self.cleaner.clean isn't callable
                result = "'{s}'".format(s=self.data)

        else:
            result = "'{s}'".format(s=self.data)

        return result

    def next(self):
        if self._iter_complete:
            raise StopIteration

        else:
            if self._index >= len(self.data):
                self._iter_complete = True

                raise StopIteration

            if self.cleaner is not None:
                try:
                    result = self.cleaner.clean(None, self.data[self._index])

                except AttributeError:
                    # self.cleaner is probably None
                    result = self.data[self._index]

                except TypeError:
                    # self.cleaner.clean isn't callable
                    result = self.data[self._index]

            else:
                result = self.data[self._index]

            self._index += 1

            return result

    def reset(self):
        self.data = self.seek(0)

    def seek(self, i=0):
        self._iter_complete = False
        self._index = i

        return self.original_data[i:]


# --------------------------------------------------
def test():
    """
    >>> from sanio.cleaners import BaseCleaner, FuncCleaner

    >>> sr = ListReader(['hello world'])
    >>> [i for i in sr]
    ['hello world']

    >>> sr = ListReader(['hello', 'world'])
    >>> [i for i in sr]
    ['hello', 'world']

    >>> sr = ListReader(['hello', 'world'])
    >>> sr
    '['hello', 'world']'

    """
    pass


## ---------------------
if __name__ == "__main__":
    import doctest
    print "Testing..."
    doctest.testmod()
    print "Done."
