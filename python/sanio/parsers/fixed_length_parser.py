from base_parser import BaseParser


class FixedLengthParser(BaseParser):
    """
    Acts as an Iterable that outputs columns of data.

    Assumes that self.reader is an Iterable that returns lines of text that
    will be split using self.frame_definitions lengths.
    """
    def __init__(self, frame_definitions=None, *args, **kwargs):
        """
        @param    frame_definitions    A tuple/list of tuples/lists of column names and counts.
        """
        self.frame_definitions = frame_definitions
        self._reader_generator = None

        super(FixedLengthParser, self).__init__(*args, **kwargs)

    def next_generator(self):
        for bit in self.reader:
            yield bit

    def next(self):
        if self._reader_generator is None:
            self._reader_generator = self.next_generator()

        # Grab the next bit of data from the reader, and split it using our
        # frame definitions.
        line = self._reader_generator.next()

        #
        # Now we split the line using the frame_definitions...
        d = dict()

        index = 0

        for tup in self.frame_definitions:
            k = tup[0]

            try:
                v = line[index:index + tup[1]].strip()

            except IndexError:
                v = line[index:].strip()

            if self.cleaner is not None:
                try:
                    d[k] = self.cleaner.clean(k, v)

                except AttributeError:
                    # self.cleaner is probably None
                    d[k] = v

                except TypeError:
                    # self.cleaner.clean isn't callable
                    d[k] = v

            else:
                d[k] = v

            try:
                index += tup[1]

            except IndexError:
                pass

        return d


# --------------------------------------------------
def test():
    """
    >>> from sanio.cleaners import StringCleaner, FuncCleaner, FuncDictCleaner
    >>> from sanio.readers import FileReader, StringReader
    >>> parser = FixedLengthParser(reader=StringReader('onetwothree'), frame_definitions=(('a', 3), ('b', 3), ('c', 5)))

    >>> [i for i in parser]
    [{'a': 'one', 'c': 'three', 'b': 'two'}]

    >>> parser = FixedLengthParser(reader=FileReader('test_data/simple.txt'), frame_definitions=(('area', 3), ('base', 3), ('ext', 4)))
    >>> [i for i in parser]
    [{'ext': '4567', 'base': '123', 'area': '555'}, {'ext': '5309', 'base': '867', 'area': '555'}, {'ext': '6543', 'base': '987', 'area': '555'}]

    >>> parser = FixedLengthParser(reader=FileReader('test_data/simple.txt'), frame_definitions=(('area', 3), ('base', 3), ('ext', 4)), cleaner=FuncCleaner(StringCleaner.safe_int))
    >>> [i for i in parser]
    [{'ext': 4567, 'base': 123, 'area': 555}, {'ext': 5309, 'base': 867, 'area': 555}, {'ext': 6543, 'base': 987, 'area': 555}]

    >>> parser = FixedLengthParser(reader=FileReader('test_data/simple.txt'), frame_definitions=(('area', 3), ('base', 3), ('ext', 4)), cleaner=FuncDictCleaner({'ext': StringCleaner.safe_int}))
    >>> [i for i in parser]
    [{'ext': 4567, 'base': '123', 'area': '555'}, {'ext': 5309, 'base': '867', 'area': '555'}, {'ext': 6543, 'base': '987', 'area': '555'}]

    """
    pass


## ---------------------
if __name__ == "__main__":
    import doctest
    print "Testing..."
    doctest.testmod()
    print "Done."
