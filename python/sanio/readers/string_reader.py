from base_reader import BaseReader


class StringReader(BaseReader):
    def __init__(self, s, *args, **kwargs):
        self.original_data = s
        self.data = self.seek(0)

        super(StringReader, self).__init__(*args, **kwargs)

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
            self._iter_complete = True

            if self.cleaner is not None:
                try:
                    result = self.cleaner.clean(None, self.data)

                except AttributeError:
                    # self.cleaner is probably None
                    result = self.data

                except TypeError:
                    # self.cleaner.clean isn't callable
                    result = self.data

            else:
                result = self.data

            return result

    def reset(self):
        self.data = self.seek(0)

    def seek(self, i=0):
        self._iter_complete = False

        return self.original_data[i:]


# --------------------------------------------------
def test():
    """
    >>> from sanio.cleaners import StringCleaner, FuncCleaner
    >>> sr = StringReader('hello world')

    >>> str(sr)
    'hello world'

    >>> sr
    'hello world'

    >>> [i for i in sr]
    ['hello world']

    >>> sr = StringReader('123456')
    >>> sr
    '123456'

    >>> [i for i in sr]
    ['123456']

    >>> sr = StringReader('123456', cleaner=FuncCleaner(StringCleaner.safe_int))
    >>> sr  # This one is cheaky, since repr() always returns a string
    '123456'

    >>> [i for i in sr]
    [123456]

    >>> sr = StringReader('hello world', cleaner=FuncCleaner(StringCleaner.super_flat))
    >>> sr
    'HELLOWORLD'

    >>> [i for i in sr]
    ['HELLOWORLD']

    """
    pass


## ---------------------
if __name__ == "__main__":
    import doctest
    print "Testing..."
    doctest.testmod()
    print "Done."
