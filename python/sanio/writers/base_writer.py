from sanio.base_sanio import BaseSanio


class BaseWriter(BaseSanio):
    def __init__(self, *args, **kwargs):
        super(BaseWriter, self).__init__(*args, **kwargs)
