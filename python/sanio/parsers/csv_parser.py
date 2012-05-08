import csv

from base_parser import BaseParser


class CSVParser(BaseParser):
    """
    Assumes that self.parser returns lines of text in CSV format, and outputs
    a Python Dictionary.
    """
    def __init__(self, *args, **kwargs):
        self._reader_generator = None

        super(CSVParser, self).__init__(*args, **kwargs)

    def __call__(self):
        return [i for i in self]

    def __getitem__(self, i):
        # Here's the worst implementation first:
        c = 0
        result = None

        while c <= i:
            try:
                result = self.next()
            except StopIteration:
                break
            else:
                c += 1

        return result

    def next_generator(self):
        for bit in csv.DictReader(self.reader):
            yield bit

    def next(self):
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

        return d


# --------------------------------------------------
def test():
    """
    >>> from sanio.cleaners import StringCleaner, FuncCleaner, FuncDictCleaner
    >>> from sanio.readers import FileReader, StringReader
    >>> from sanio.transformers import DictTransform

    # This one still fails... Not sure how to fake a multi-line CSV within a String in a doctest line.
    >>> parser = CSVParser(reader=StringReader('''"a","b","c"\
    >>> "one","two","3"\
    >>> '''))
    >>> [i for i in parser]  # Parsing using a StringReader
    [{'a': 'one', 'c': '3', 'b': 'two'}]

    >>> parser = CSVParser(reader=FileReader('test_data/simple.csv'))
    >>> [i for i in parser]
    [{'a': 'one', 'c': '3', 'b': 'two'}]

    >>> parser = CSVParser(reader=FileReader('test_data/simple.csv'), cleaner=FuncCleaner(StringCleaner.safe_int))
    >>> [i for i in parser]
    [{'a': None, 'c': 3, 'b': None}]

    >>> parser = CSVParser(reader=FileReader('test_data/simple.csv'), cleaner=FuncDictCleaner({'c': StringCleaner.safe_int}))
    >>> [i for i in parser]
    [{'a': 'one', 'c': 3, 'b': 'two'}]

    >>> parser = CSVParser(reader=FileReader('test_data/simple.csv'), cleaner=FuncDictCleaner({'c': StringCleaner.safe_int}))
    >>> parser()  # Testing __call__
    [{'a': 'one', 'c': 3, 'b': 'two'}]

    >>> parser = CSVParser(reader=FileReader('test_data/numbers.csv'))
    >>> [i for i in parser]
    [{'Volume': '12244871', 'Day Change': '-15.08', 'Price': '587.92', 'High': '598.40', 'SMBL': 'AAPL', 'Low': '584.75', 'Time': '1:54pm', 'Date': '4/30/2012', 'Open': '597.94'}, {'Volume': '1022507', 'Day Change': '-7.09', 'Price': '607.89', 'High': '616.082', 'SMBL': 'GOOG', 'Low': '607.67', 'Time': '1:55pm', 'Date': '4/30/2012', 'Open': '612.99'}, {'Volume': '4504323', 'Day Change': '-3.18', 'Price': '80.56', 'High': '83.8723', 'SMBL': 'NFLX', 'Low': '80.10', 'Time': '1:56pm', 'Date': '4/30/2012', 'Open': '82.61'}]

    >>> parser = CSVParser(reader=FileReader('test_data/numbers.csv'))
    >>> [i['SMBL'] for i in parser]
    ['AAPL', 'GOOG', 'NFLX']

    >>> parser = DictTransform(reader=CSVParser(reader=FileReader('test_data/numbers.csv')), remap_fields={'SMBL': 'Symbol'})
    >>> [i['Symbol'] for i in parser]
    ['AAPL', 'GOOG', 'NFLX']

    >>> [i['Symbol'] for i in DictTransform(reader=CSVParser(reader=FileReader('test_data/numbers.csv')), remap_fields={'SMBL': 'Symbol'})]
    ['AAPL', 'GOOG', 'NFLX']

    >>> parser = CSVParser(reader=FileReader('test_data/numbers.csv'))
    >>> parser[0]['SMBL']
    'AAPL'

    >>> parser[0]['SMBL']
    'AAPL'

    >>> parser[1]['SMBL']
    'GOOG'

    >>> parser = CSVParser(reader=FileReader('test_data/numbers.csv'))
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
