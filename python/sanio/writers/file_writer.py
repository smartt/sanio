import codecs
import os

from sanio.base import BaseSanio
from sanio import fields


class BaseWriter(BaseSanio):
    def delete(self):
        try:
            os.unlink(self.filename)
        except IOError:
            # Crap
            pass


class FileWriter(BaseWriter):
    filename = fields.StringField()

    def __init__(self, *args, **kwargs):
        super(FileWriter, self).__init__(*args, **kwargs)

        with open(self.filename, "w") as fp:
            try:
                for line in self.data_source:
                    if isinstance(line, (dict,)):
                        fp.write(self._clean(str(line)))
                    else:
                        fp.write(self._clean(line))

                    fp.write(os.linesep)

            except StopIteration:
                return


class UTF8Writer(BaseWriter):
    filename = fields.StringField()

    def __init__(self, filename, *args, **kwargs):
        super(UTF8Writer, self).__init__(*args, **kwargs)

        with codecs.open(self.filename, "w", "utf-8") as fp:
            try:
                for line in self.data_source:
                    fp.write(self._clean(line))
                    fp.write(os.linesep)

            except StopIteration:
                return
