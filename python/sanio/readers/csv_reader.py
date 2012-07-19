import csv

from sanio.base_sanio import BaseSanio


class CSVReader(BaseSanio):
    """
    Assumes that self.parser returns lines of text in CSV format, and outputs
    a Python Dictionary.
    """
    # def __init__(self, *args, **kwargs):
    #     super(CSVReader, self).__init__(*args, **kwargs)

    def __call__(self):
        return [i for i in self]

    def __getitem__(self, n):
        # Here's the worst implementation first:
        # We iterate over the value of self.next() (throwing the response away)
        # until we get to the nth result, which we return.
        # If the iterator runs out of data before we see the nth value, return
        # None.
        c = 0
        result = None

        while c <= n:
            try:
                result = self.next()
            except StopIteration:
                break
            else:
                c += 1

        return result

    def next_generator(self):
        for bit in csv.DictReader(self.data_source):
            yield bit

    def next(self):
        # 'd' is going to be a Dictionary, but we're doing this ugly
        # hack to kick-start the `while` loop.
        d = {'hack': True}

        # We're looping here to account for rows that might be deleted by the
        # specified filters (and since we don't have tail-call optimization for
        # recursion, we don't want to blow the stack repeatedly calling next().)
        while d is not None:
            if self._reader_generator is None:
                self._reader_generator = self.next_generator()

            # Grab the next bit of data from the reader, and split it using our
            # frame definitions.
            d = self._reader_generator.next()

            if self.cleaner is not None:
                try:
                    for k, v in d.items():
                        d[k] = self.cleaner.clean(k, v)

                except AttributeError:
                    # self.cleaner is probably None
                    pass

                except TypeError:
                    # self.cleaner.clean isn't callable
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
    >>> from sanio.transformers import DictTransform

    # This one still fails... Not sure how to fake a multi-line CSV within a String in a doctest line.
    # >>> parser = CSVReader(data_source=StringReader('''"a","b","c"\
    # >>> "one","two","3"\
    # >>> '''))
    # >>> [i for i in parser]  # Parsing using a StringReader
    # [{'a': 'one', 'c': '3', 'b': 'two'}]

    >>> parser = CSVReader(data_source=FileReader('test_data/simple.csv'))
    >>> [i for i in parser]
    [{'a': 'one', 'c': '3', 'b': 'two'}]

    >>> parser = CSVReader(data_source=FileReader('test_data/simple.csv'), cleaner=FuncCleaner(StringCleaner.safe_int))
    >>> [i for i in parser]
    [{'a': None, 'c': 3, 'b': None}]

    >>> parser = CSVReader(data_source=FileReader('test_data/simple.csv'), cleaner=FuncDictCleaner({'c': StringCleaner.safe_int}))
    >>> [i for i in parser]
    [{'a': 'one', 'c': 3, 'b': 'two'}]

    >>> parser = CSVReader(data_source=FileReader('test_data/simple.csv'), cleaner=FuncDictCleaner({'c': StringCleaner.safe_int}))
    >>> parser()  # Testing __call__
    [{'a': 'one', 'c': 3, 'b': 'two'}]

    >>> parser = CSVReader(data_source=FileReader('test_data/numbers.csv'))
    >>> [i for i in parser]
    [{'Volume': '12244871', 'Day Change': '-15.08', 'Price': '587.92', 'High': '598.40', 'SMBL': 'AAPL', 'Low': '584.75', 'Time': '1:54pm', 'Date': '4/30/2012', 'Open': '597.94'}, {'Volume': '1022507', 'Day Change': '-7.09', 'Price': '607.89', 'High': '616.082', 'SMBL': 'GOOG', 'Low': '607.67', 'Time': '1:55pm', 'Date': '4/30/2012', 'Open': '612.99'}, {'Volume': '4504323', 'Day Change': '-3.18', 'Price': '80.56', 'High': '83.8723', 'SMBL': 'NFLX', 'Low': '80.10', 'Time': '1:56pm', 'Date': '4/30/2012', 'Open': '82.61'}]

    >>> parser = CSVReader(data_source=FileReader('test_data/numbers.csv'))
    >>> [i['SMBL'] for i in parser]
    ['AAPL', 'GOOG', 'NFLX']

    >>> parser = DictTransform(data_source=CSVReader(data_source=FileReader('test_data/numbers.csv')), remap_fields={'SMBL': 'Symbol'})
    >>> [i['Symbol'] for i in parser]
    ['AAPL', 'GOOG', 'NFLX']

    >>> [i['Symbol'] for i in DictTransform(data_source=CSVReader(data_source=FileReader('test_data/numbers.csv')), remap_fields={'SMBL': 'Symbol'})]
    ['AAPL', 'GOOG', 'NFLX']

    >>> parser = CSVReader(data_source=FileReader('test_data/numbers.csv'))
    >>> parser[0]['SMBL']
    'AAPL'

    >>> parser[0]['SMBL']
    'AAPL'

    >>> parser[1]['SMBL']
    'GOOG'

    >>> parser = CSVReader(data_source=FileReader('test_data/numbers.csv'))
    >>> parser[2]['SMBL']
    'NFLX'

    >>> parser[0]['SMBL']
    'AAPL'

    """
    pass


## ---------------------
if __name__ == "__main__":
    import doctest
    print "Testing..."
    doctest.testmod()
    print "Done."
