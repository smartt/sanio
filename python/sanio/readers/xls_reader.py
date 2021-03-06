try:
    import xlrd
except ImportError:
    _HAS_XLRD = False
else:
    _HAS_XLRD = True

from sanio.base import BaseSanio
from sanio import fields


class XLSReader(BaseSanio):
    filename = fields.StringField()
    wb = fields.ObjectField(null=True)
    _next_line = fields.StringField(null=True)

    def _setup(self):
        if _HAS_XLRD:
            self.wb = xlrd.open_workbook(self.filename)
            self.sheet_count = self.wb.nsheets
            self.sheet_names = self.wb.sheet_names()
            self.current_sheet = self.wb.sheet_by_index(0)

    def next_line(self):
        if self.wb is None:
            self._setup()

        for row_count in range(0, self.current_sheet.nrows):
            line_bits = []

            for cell_count in range(0, self.current_sheet.ncols):
                # line_bits.append(self.current_sheet.cell(rowx=row_count, colx=cell_count).value)
                v = self.current_sheet.cell_value(rowx=row_count, colx=cell_count)

                if not isinstance(v, (unicode, str)):
                    v = unicode(v)

                line_bits.append(v)

            yield ','.join(line_bits)

    def next(self):
        if not _HAS_XLRD:
            raise StopIteration

        if self._next_line is None:
            self._next_line = self.next_line()

        line = self._next_line.next()

        if self.cleaner is not None:
            try:
                line = self.cleaner.clean(None, line)

            except AttributeError:
                # self.cleaner is probably None
                pass

            except TypeError:
                # self.cleaner.clean isn't callable
                pass

        return line

# """
#     sh = book.sheet_by_index(0)
#     print sh.name, sh.nrows, sh.ncols
#     print "Cell D30 is", sh.cell_value(rowx=29, colx=3)
#     for rx in range(sh.nrows):
#         print sh.row(rx)
#     ----------

# sh = wb.sheet_by_index(0)
# sh = wb.sheet_by_name(u'Sheet1')
# Iterate through rows, returning each as a list that you can index:

# for rownum in range(sh.nrows):
#     print sh.row_values(rownum)
# If you just want the first column:

# first_column = sh.col_values(0)
# Index individual cells:

# cell_A1 = sh.cell(0,0).value
# cell_C4 = sh.cell(rowx=3,colx=2).value
# (Note Python indices start at zero but Excel starts at one)

# """
