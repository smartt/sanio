#!/usr/bin/env python

from sanio.base_sanio import BaseSanio


class FTPWriter(BaseSanio):
    def __init__(self, *args, **kwargs):
        super(FTPWriter, self).__init__(*args, **kwargs)


class SFTPWriter(BaseSanio):
    def __init__(self, *args, **kwargs):
        super(SFTPWriter, self).__init__(*args, **kwargs)

# --------------------------------------------------
#               MAIN
# --------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
