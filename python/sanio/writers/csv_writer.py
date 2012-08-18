#!/usr/bin/env python
import os

from sanio.writers.file_writer import BaseWriter
from sanio import fields


class CSVWriter(BaseWriter):
    filename = fields.StringField()

    def __init__(self, *args, **kwargs):
        super(CSVWriter, self).__init__(*args, **kwargs)

        with open(self.filename, "w") as fp:
            try:
                for line in self.data_source:
                    if isinstance(line, (dict,)):
                        if 'fieldnames' in kwargs:
                            bits = []

                            for k in kwargs['fieldnames']:
                                bits.append(line[k])

                            if 'delimiter' in kwargs:
                                use_delimiter = kwargs['delimiter']
                            else:
                                use_delimiter = ','

                            line = use_delimiter.join(bits)

                    fp.write(self._clean(line))

                    fp.write(os.linesep)

            except StopIteration:
                return
