from sanio.base_sanio import BaseSanio


class GeoValidator(BaseSanio):
    def __init__(self, *args, **kwargs):
        super(GeoValidator, self).__init__(*args, **kwargs)

    @classmethod
    def is_valid_address(cls, s):
        return False

    @classmethod
    def is_valid_zipcode(cls, s):
        return False
