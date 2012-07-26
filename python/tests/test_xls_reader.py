import unittest

from sanio.readers import XLSReader


class TestXLSReader(unittest.TestCase):
    def test_simple(self):
        fr = XLSReader('test_data/simple.xls')

        self.assertEqual(
            [i for i in fr],
            [u'One,Two,Three,Four', u'1.0,2.0,3.0,4.0', u'a,b,c,d', u'fe,fi,fo,fum']
        )


if __name__ == '__main__':
    unittest.main()
