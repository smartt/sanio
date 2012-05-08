from base_parser import BaseParser


class DictParser(BaseParser):
    """
    A DictParser takes in a Python Dictionary, and returns a Python Dictionary.
    The most useful application is converting the structure (e.g., renaming fields.)
    """
    def __init__(self, *args, **kwargs):
        super(DictParser, self).__init__(*args, **kwargs)
