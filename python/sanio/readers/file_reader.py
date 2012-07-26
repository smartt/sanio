import codecs

from sanio.base import BaseSanio


class BaseReader(BaseSanio):
    def next(self):
        if self._next_line is None:
            self._next_line = self.next_line()

        return self._filter(self._clean(self._next_line.next()))


class FileReader(BaseReader):
    def __init__(self, filename, *args, **kwargs):
        self.filename = filename
        self._next_line = None

        super(FileReader, self).__init__(*args, **kwargs)

    def next_line(self):
            with open(self.filename, 'r') as fp:
                for line in fp.readlines():
                    yield line.rstrip('\n')


class UTF16FileReader(BaseReader):
    def __init__(self, filename, blocksize=1048576, *args, **kwargs):
        self.filename = filename
        self._next_line = None
        self.BLOCKSIZE = blocksize

        super(UTF16FileReader, self).__init__(*args, **kwargs)

    def next_line(self):
        with codecs.open(self.filename, "r", "utf-16") as fp:
            while True:
                contents = fp.read(self.BLOCKSIZE)

                if not contents:
                    raise StopIteration

                yield contents
