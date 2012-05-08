import codecs

from base_reader import BaseReader


class FileReader(BaseReader):
    def __init__(self, filename, *args, **kwargs):
        self.filename = filename
        self._next_line = None

        super(FileReader, self).__init__(*args, **kwargs)

    def next_line(self):
            with open(self.filename, 'r') as fp:
                for line in fp.readlines():
                    yield line.rstrip('\n')

    def next(self):
        if self._next_line is None:
            self._next_line = self.next_line()

        line = self._next_line.next()

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


class UTF16Reader(BaseReader):
    def __init__(self, filename, *args, **kwargs):
        self.filename = filename
        self._next_line = None
        self.BLOCKSIZE = 1048576  # or some other, desired size in bytes

        super(UTF16Reader, self).__init__(*args, **kwargs)

    def next_line(self):
        with codecs.open(self.filename, "r", "utf-16") as fp:
            while True:
                contents = fp.read(self.BLOCKSIZE)

                if not contents:
                    raise StopIteration

                yield contents

    def next(self):
        if self._next_line is None:
            self._next_line = self.next_line()

        line = self._next_line.next()

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


def file_test():
    """
    >>> fr = FileReader('test_data/simple.txt')

    >>> [i for i in fr]
    ['One, two, three shows how', 'Serial commas are good', 'Correcting grammar']

    """
    pass


## ---------------------
if __name__ == "__main__":
    import doctest
    print "Testing..."
    doctest.testmod()
    print "Done."
