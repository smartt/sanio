#!/usr/bin/env python

from sanio.base import BaseSanio


class XMLWriter(BaseSanio):
    def __init__(self, *args, **kwargs):
        super(XMLWriter, self).__init__(*args, **kwargs)

# --------------------------------------------------
#               MAIN
# --------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
