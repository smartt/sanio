from sanio.validators import NumericValidator


def test():
    """
    >>> NumericValidator.is_float('TX')
    False

    >>> NumericValidator.is_float('1')
    False

    >>> NumericValidator.is_float(1)
    False

    >>> NumericValidator.is_float('3.14')
    True

    >>> NumericValidator.is_float(3.14)
    True

    >>> NumericValidator.is_integer('TX')
    False

    >>> NumericValidator.is_integer('1')
    True

    >>> NumericValidator.is_integer(1)
    True

    >>> NumericValidator.is_integer('3.14')
    False

    >>> NumericValidator.is_integer(3.14)
    False

    >>> NumericValidator.is_numeric('TX')
    False

    >>> NumericValidator.is_numeric('  TX ')
    False

    >>> NumericValidator.is_numeric('1')
    True

    >>> NumericValidator.is_numeric(1)
    True

    >>> NumericValidator.is_numeric(3.14)
    True

    >>> NumericValidator.is_numeric('3.14')
    True

    """
    pass

## ---------------------
if __name__ == "__main__":
    import doctest
    print "Testing..."
    doctest.testmod()
    print "Done."
