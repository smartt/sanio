#!/usr/bin/env python

from sanio.base import BaseSanio


class FixedLengthWriter(BaseSanio):
    def __init__(self, *args, **kwargs):
        super(FixedLengthWriter, self).__init__(*args, **kwargs)

# --------------------------------------------------
#               MAIN
# --------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
