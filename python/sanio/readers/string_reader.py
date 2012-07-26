from sanio.base import BaseSanio


class StringReader(BaseSanio):
    def __init__(self, s, *args, **kwargs):
        self.original_data = s
        self.data = self.seek(0)

        super(StringReader, self).__init__(*args, **kwargs)

    def __str__(self):
        return self.data

    def __unicode__(self):
        return self.data

    def __repr__(self):
        result = None

        if self.cleaner is not None:
            try:
                result = "'{s}'".format(s=self.cleaner.clean(None, self.data))

            except AttributeError:
                # self.cleaner is probably None
                result = "'{s}'".format(s=self.data)

            except TypeError:
                # self.cleaner.clean isn't callable
                result = "'{s}'".format(s=self.data)

        else:
            result = "'{s}'".format(s=self.data)

        return result

    def next(self):
        if self._iter_complete:
            raise StopIteration

        else:
            self._iter_complete = True

            return self._filter(self._clean(self.data))

    def reset(self):
        self.data = self.seek(0)

    def seek(self, i=0):
        self._iter_complete = False

        return self.original_data[i:]
