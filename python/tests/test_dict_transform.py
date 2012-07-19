from sanio.transformers import DictTransform
from sanio.readers import ListReader


# --------------------------------------------------
def test():
    """
    >>> parser = DictTransform(data_source=ListReader([{'foo': 1, 'blah': 2}]), remap_fields={'foo': 'bar'})
    >>> [i['bar'] for i in parser]
    [1]

    >>> parser = DictTransform(data_source=ListReader([{'foo': 1, 'blah': 2}]), remap_fields={'foo': 'bar'})
    >>> [i for i in parser]
    [{'blah': 2, 'bar': 1}]

    >>> parser = DictTransform(data_source=ListReader([{'foo': 1, 'blah': ''}]), remap_fields={'foo': 'bar'})
    >>> [i for i in parser]
    [{'blah': '', 'bar': 1}]

    >>> parser = NonSparseDictTransform(data_source=ListReader([{'foo': 1, 'blah': ''}]), remap_fields={'foo': 'bar'})
    >>> [i for i in parser]
    [{'bar': 1}]

    """
    pass


## ---------------------
if __name__ == "__main__":
    import doctest
    print "Testing..."
    doctest.testmod()
    print "Done."
