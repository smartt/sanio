#!/usr/bin/env python

from sanio.base_sanio import BaseSanio


class YammerWriter(BaseSanio):
    def __init__(self, *args, **kwargs):
        super(YammerWriter, self).__init__(*args, **kwargs)

# --------------------------------------------------
#               MAIN
# --------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
