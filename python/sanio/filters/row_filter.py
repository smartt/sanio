import random

from sanio.base import BaseSanio
from sanio import fields


class RowFilter(BaseSanio):
    field = fields.StringField(null=True)
    fn = fields.FunctionField(null=True)

    @classmethod
    def random_filter(self, d):
        """
        A coin-toss filter that you can use to randomly keep/omit lines of data.
        """
        random.seed()

        if random.randint(0, 9) > 5:
            return True
        else:
            return False

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
