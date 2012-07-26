#!/usr/bin/env python

from sanio.base import BaseSanio


class NumericCleaner(BaseSanio):
    def __init__(self, *args, **kwargs):
        super(NumericCleaner, self).__init__(*args, **kwargs)
