import csv

from sanio.base_sanio import BaseSanio


class CSVReader(BaseSanio):
    """
    Assumes that self.parser returns lines of text in CSV format, and outputs
    a Python Dictionary.
    """
    def __init__(self, *args, **kwargs):
        self.delimiter = ','
        self.quotechar = '"'

        super(CSVReader, self).__init__(*args, **kwargs)

        if 'quoting' in kwargs:
            if kwargs['quoting'] == 'all':
                self.quoting = csv.QUOTE_ALL

            elif kwargs['quoting'] == 'minimal':
                self.quoting = csv.QUOTE_MINIMAL

            elif kwargs['quoting'] == 'nonnumeric':
                self.quoting = csv.QUOTE_NONNUMERIC

            elif kwargs['quoting'] == 'none':
                self.quoting = csv.QUOTE_NONE

        else:
            self.quoting = csv.QUOTE_ALL

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
        if self.data_source is not None:
            for bit in csv.DictReader(self.data_source, delimiter=self.delimiter, quotechar=self.quotechar, quoting=self.quoting):
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

            # Grab the next bit of data from the reader
            return self._filter(self._clean(self._reader_generator.next()))

        return d
