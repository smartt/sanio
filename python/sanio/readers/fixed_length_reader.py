from sanio.base import BaseSanio
from sanio import fields


class FixedLengthReader(BaseSanio):
    """
    Acts as an Iterable that outputs columns of data.

    Assumes that self.data_source is an Iterable that returns lines of text that
    will be split using self.frame_definitions lengths.

    @param    frame_definitions    A tuple/list of tuples/lists of column names and counts.
    """
    frame_definitions = fields.TupleField(null=True)

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

                d[k] = self._clean({k: v})

                try:
                    index += tup[1]

                except IndexError:
                    pass

            d = self._filter(d)

        return d
