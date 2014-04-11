#!/usr/bin/env python
from datetime import datetime, date

from sanio.base import BaseSanio


class DateTimeCleaner(BaseSanio):
    def __init__(self, *args, **kwargs):
        super(DateTimeCleaner, self).__init__(*args, **kwargs)

    @classmethod
    def extract_date_by_pattern(cls, s, pattern, return_match_str=False):
        #print('DateTimeCleaner(s="{s}", pattern="{p}")'.format(s=s, p=pattern))
        # tokenize..
        bits = s.split(' ')
        d = None

        # and scan..
        for bit in bits:
            try:
                parsed_date = datetime.strptime(bit, pattern).date()
            except ValueError:
                continue
            else:
                if parsed_date.year == 1900:
                    d = date(datetime.now().year, parsed_date.month, parsed_date.day)
                else:
                    d = date(parsed_date.year, parsed_date.month, parsed_date.day)

                break

        if return_match_str:
            return d, bit
        else:
            return d

# --------------------------------------------------
#               MAIN
# --------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
