from sanio.base_sanio import BaseSanio


class RowFilter(BaseSanio):
    def __init__(self, field=None, function=None, *args, **kwargs):
        self.field = field
        self.fn = function

        super(RowFilter, self).__init__(*args, **kwargs)

    def filter(self, d):
        # If we have a field to work on, run the function just on that field.
        # If the function returns True, keep the field; Otherwise, delete it.
        if self.field is not None:
            try:
                reject_row = self.fn(d[self.field])

            except AttributeError:
                pass

            except TypeError:
                pass

            else:
                if reject_row is False:
                    return None

        else:
            # If we don't have a field, then we're running the function against
            # every cell. If *any* of the calls to self.fn return False, we drop
            # the row (by returning None); Otherwise, return the whole structure.
            reject_row = False

            for k, v in d.items():
                try:
                    reject_row = self.fn(v)

                except AttributeError:
                    continue

                except TypeError:
                    continue

                else:
                    if reject_row is False:
                        return None

        return d
