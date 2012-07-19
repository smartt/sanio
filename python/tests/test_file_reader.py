from sanio.readers import FileReader


def file_test():
    """
    >>> fr = FileReader('test_data/simple.txt')

    >>> [i for i in fr]
    ['One, two, three shows how', 'Serial commas are good', 'Correcting grammar']

    """
    pass


## ---------------------
if __name__ == "__main__":
    import doctest
    print "Testing..."
    doctest.testmod()
    print "Done."
