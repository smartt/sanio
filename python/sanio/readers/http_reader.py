import requests
# from requests.auth import HTTPBasicAuth
# from requests.auth import HTTPDigestAuth

from sanio.base_sanio import BaseSanio


class HTTPReader(BaseSanio):
    def __init__(self, url, *args, **kwargs):
        self.url = url

        super(HTTPReader, self).__init__(*args, **kwargs)

    def _fetch(self, method='GET', args=None):
        if self.url is not None:
            r = None

            # args = {'key1': 'value1', 'key2': 'value2'}
            # headers = {'content-type': 'application/json'}
            # r = requests.get(self.url, params=args)
            # r = requests.get(self.url, params=args, headers=headers)

            # requests.get('https://api.github.com/user', auth=HTTPBasicAuth('user', 'pass'))

            # requests.get(self.url, auth=HTTPDigestAuth('user', 'pass'))

            # requests.get('http://github.com', timeout=60)

            # http://pypi.python.org/pypi/requests-oauth

            if method == 'GET':
                r = requests.get(self.url)

            elif method == 'POST':
                r = requests.post(self.url)

                # claimed_data_transfered = r.headers['content-length']

            if r is not None:
                # if r.status_code == 200:
                return r.text

    def next(self):
        if self._iter_complete:
            raise StopIteration

        else:
            self._iter_complete = True

            return self._filter(self._clean(self._fetch().next()))
