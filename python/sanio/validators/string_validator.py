from sanio.base_sanio import BaseSanio


class StringValidator(BaseSanio):
    def __init__(self, *args, **kwargs):
        super(StringValidator, self).__init__(*args, **kwargs)

    @classmethod
    def is_empty(cls, s):
        """
        >>> StringValidator.is_empty('TX')
        False

        >>> StringValidator.is_empty('  TX ')
        False

        >>> StringValidator.is_empty('')
        True

        >>> StringValidator.is_empty('   ')
        True

        """
        return False
