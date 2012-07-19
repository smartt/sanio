#!/usr/bin/env python

from sanio.base_sanio import BaseSanio


class EmailWriter(BaseSanio):
    def __init__(self, *args, **kwargs):
        super(EmailWriter, self).__init__(*args, **kwargs)

# --------------------------------------------------
#               MAIN
# --------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
