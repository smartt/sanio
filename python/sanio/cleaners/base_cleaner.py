

class BaseCleaner(object):
    def __init__(self, *args, **kwargs):
        # self.verbose = verbose
        self.cleaner = None
        self.reader = None
        self.verbose = False

        for k, v in kwargs.items():
            self.__dict__[k] = v

    def clean(self, key=None, value=None):
        """
        Does nothing valuable. Over-ride this!
        """
        return value


## ---------------------
if __name__ == "__main__":
    import doctest
    print "Testing..."
    doctest.testmod()
    print "Done."
