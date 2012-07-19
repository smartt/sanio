from sanio.base_sanio import BaseSanio


class DictReader(BaseSanio):
    """
    A DictReader takes in a Python Dictionary, and returns a Python Dictionary.
    The most useful application is converting the structure (e.g., renaming fields.)
    """
    def __init__(self, *args, **kwargs):
        super(DictReader, self).__init__(*args, **kwargs)
