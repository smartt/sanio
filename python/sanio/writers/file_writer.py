import codecs
import os

from sanio.base import BaseSanio


class BaseWriter(BaseSanio):
    def delete(self):
        try:
            os.unlink(self.filename)
        except IOError:
            # Crap
            pass


class FileWriter(BaseWriter):
    def __init__(self, filename, *args, **kwargs):
        self.filename = filename

        super(FileWriter, self).__init__(*args, **kwargs)

        with open(self.filename, "w") as fp:
            try:
                for line in self.data_source:
                    fp.write(self._clean(line))
                    fp.write(os.linesep)

            except StopIteration:
                return


class UTF8Writer(BaseWriter):
    def __init__(self, filename, *args, **kwargs):
        self.filename = filename

        super(UTF8Writer, self).__init__(*args, **kwargs)

        with codecs.open(self.filename, "w", "utf-8") as fp:
            try:
                for line in self.data_source:
                    fp.write(self._clean(line))
                    fp.write(os.linesep)

            except StopIteration:
                return
