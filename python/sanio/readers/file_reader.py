import codecs

from sanio import fields
from sanio.base import BaseSanio


class BaseReader(BaseSanio):
    def next(self):
        if self._next_line is None:
            self._next_line = self.next_line()

        return self._filter(self._clean(self._next_line.next()))


class FileReader(BaseReader):
    filename = fields.StringField()
    _next_line = fields.StringField(null=True)

    def next_line(self):
            with open(self.filename, 'r') as fp:
                for line in fp.readlines():
                    yield line.rstrip('\n')


class UTF16FileReader(BaseReader):
    filename = fields.StringField()
    blocksize = fields.IntegerField(default=1048576)
    _next_line = fields.StringField(null=True)

    def next_line(self):
        with codecs.open(self.filename, "r", "utf-16") as fp:
            while True:
                contents = fp.read(self.blocksize)

                if not contents:
                    raise StopIteration

                yield contents
