from sanio.base_sanio import BaseSanio


class HTTPReader(BaseSanio):
    def __init__(self, url, *args, **kwargs):
        self.url = url

        super(HTTPReader, self).__init__(*args, **kwargs)
