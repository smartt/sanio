import codecs
import os

from base_writer import BaseWriter


class FileWriter(BaseWriter):
    def __init__(self, *args, **kwargs):
        super(FileWriter, self).__init__(*args, **kwargs)

    def save(self, filename):
        with open(filename, "w") as fp:
            try:
                for line in self.reader:
                    fp.write(self._clean(line))
                    fp.write(os.linesep)

            except StopIteration:
                return


class UTF8Writer(BaseWriter):
    def __init__(self, *args, **kwargs):
        self._next_line = None

        super(UTF8Writer, self).__init__(*args, **kwargs)

    def save(self, filename):
        with codecs.open(filename, "w", "utf-8") as fp:
            try:
                for line in self.reader:
                    fp.write(self._clean(line))
                    fp.write(os.linesep)

            except StopIteration:
                return
