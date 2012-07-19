import codecs

from sanio.base_sanio import BaseSanio


class FileReader(BaseSanio):
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

        line = self._clean(line)

        return line


class UTF16FileReader(BaseSanio):
    def __init__(self, filename, *args, **kwargs):
        self.filename = filename
        self._next_line = None
        self.BLOCKSIZE = 1048576  # or some other, desired size in bytes

        super(UTF16FileReader, self).__init__(*args, **kwargs)

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

        line = self._clean(line)

        return line
