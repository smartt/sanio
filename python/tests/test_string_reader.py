from sanio.cleaners import StringCleaner
from sanio.mappers import FuncMapper
from sanio.readers import StringReader


def test():
    """
    >>> sr = StringReader('hello world')

    >>> str(sr)
    'hello world'

    >>> sr
    'hello world'

    >>> [i for i in sr]
    ['hello world']

    >>> sr = StringReader('123456')
    >>> sr
    '123456'

    >>> [i for i in sr]
    ['123456']

    >>> sr = StringReader('123456', cleaner=FuncCleaner(StringCleaner.safe_int))
    >>> sr  # This one is cheaky, since repr() always returns a string
    '123456'

    >>> [i for i in sr]
    [123456]

    >>> sr = StringReader('hello world', cleaner=FuncMapper(StringCleaner.super_flat))
    >>> sr
    'HELLOWORLD'

    >>> [i for i in sr]
    ['HELLOWORLD']

    """
    pass


## ---------------------
if __name__ == "__main__":
    import doctest
    print "Testing..."
    doctest.testmod()
    print "Done."
