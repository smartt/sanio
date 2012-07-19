from sanio.base_sanio import BaseSanio


class NumericAggregator(BaseSanio):
    def __init__(self, *args, **kwargs):
        super(NumericAggregator, self).__init__(*args, **kwargs)

    @classmethod
    def average(cls, series):
        return None

    @classmethod
    def max(cls, series):
        return None

    @classmethod
    def median(cls, series):
        return None

    @classmethod
    def min(cls, series):
        return None

    @classmethod
    def percent_of_average(cls, value, series):
        return None
