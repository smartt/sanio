#!/usr/bin/env python

from sanio.base_sanio import BaseSanio


class FTPReader(BaseSanio):
    def __init__(self, *args, **kwargs):
        super(FTPReader, self).__init__(*args, **kwargs)


class SFTPReader(BaseSanio):
    def __init__(self, *args, **kwargs):
        super(SFTPReader, self).__init__(*args, **kwargs)

# --------------------------------------------------
#               MAIN
# --------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
