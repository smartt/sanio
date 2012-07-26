#!/usr/bin/env python

from sanio.base import BaseSanio


class ColumnFilter(BaseSanio):
    def __init__(self, *args, **kwargs):
        super(ColumnFilter, self).__init__(*args, **kwargs)
