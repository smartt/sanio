from sanio.base_sanio import BaseSanio


class FixedLengthReader(BaseSanio):
    """
    Acts as an Iterable that outputs columns of data.

    Assumes that self.data_source is an Iterable that returns lines of text that
    will be split using self.frame_definitions lengths.
    """
    def __init__(self, frame_definitions=None, *args, **kwargs):
        """
        @param    frame_definitions    A tuple/list of tuples/lists of column names and counts.
        """
        self.frame_definitions = frame_definitions

        super(FixedLengthReader, self).__init__(*args, **kwargs)

    def next_generator(self):
        for bit in self.data_source:
            yield bit

    def next(self):
        # 'd' is going to be a Dictionary, but we're doing this ugly
        # hack to kick-start the `while` loop.
        d = {'hack': True}

        # We're looping here to account for rows that might be deleted by the
        # specified filters.
        while d is not None:
            if self._reader_generator is None:
                self._reader_generator = self.next_generator()

            # Grab the next bit of data from the data_source, and split it using our
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

            if self.filter is not None:
                # Run the filter on the row
                try:
                    d = self.filter.filter(d)

                except AttributeError:
                    # self.filter is probably None
                    pass

                except TypeError:
                    # self.filter.filter isn't callable
                    pass

        return d


# --------------------------------------------------
def test():
    """
    >>> from sanio.cleaners import StringCleaner, FuncCleaner, FuncDictCleaner
    >>> from sanio.readers import FileReader, StringReader
    >>> parser = FixedLengthReader(data_source=StringReader('onetwothree'), frame_definitions=(('a', 3), ('b', 3), ('c', 5)))

    >>> [i for i in parser]
    [{'a': 'one', 'c': 'three', 'b': 'two'}]

    >>> parser = FixedLengthReader(data_source=FileReader('test_data/simple.txt'), frame_definitions=(('area', 3), ('base', 3), ('ext', 4)))
    >>> [i for i in parser]
    [{'ext': '4567', 'base': '123', 'area': '555'}, {'ext': '5309', 'base': '867', 'area': '555'}, {'ext': '6543', 'base': '987', 'area': '555'}]

    >>> parser = FixedLengthReader(data_source=FileReader('test_data/simple.txt'), frame_definitions=(('area', 3), ('base', 3), ('ext', 4)), cleaner=FuncCleaner(StringCleaner.safe_int))
    >>> [i for i in parser]
    [{'ext': 4567, 'base': 123, 'area': 555}, {'ext': 5309, 'base': 867, 'area': 555}, {'ext': 6543, 'base': 987, 'area': 555}]

    >>> parser = FixedLengthReader(data_source=FileReader('test_data/simple.txt'), frame_definitions=(('area', 3), ('base', 3), ('ext', 4)), cleaner=FuncDictCleaner({'ext': StringCleaner.safe_int}))
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
