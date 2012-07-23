import unittest

from sanio.readers import FileReader


class TestFileReader(unittest.TestCase):
    def test_simple(self):
        fr = FileReader('tests/test_data/simple.txt')

        self.assertEqual([i for i in fr], ['One, two, three shows how', 'Serial commas are good', 'Correcting grammar'])


if __name__ == '__main__':
    unittest.main()
