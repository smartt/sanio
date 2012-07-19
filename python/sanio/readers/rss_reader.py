from sanio.base_sanio import BaseSanio


class RSSReader(BaseSanio):
    """
    Assumes that self.parser returns lines of text in RSS format, and outputs
    a Python Dictionary.
    """
    def __init__(self, *args, **kwargs):
        self._reader_generator = None

        super(RSSReader, self).__init__(*args, **kwargs)
