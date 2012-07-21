import unittest

from sanio.readers import FileReader
from sanio.writers import FileWriter


class TestFileReadWrite(unittest.TestCase):
    def test_simple(self):
        input_path = 'tests/test_data/simple.txt'
        tmp_save_path = 'tmp_test_simple.txt'

        initial_fr = FileReader(input_path)
        self.assertEqual([i for i in initial_fr], ['One, two, three shows how', 'Serial commas are good', 'Correcting grammar'])

        fw = FileWriter(filename=tmp_save_path, data_source=initial_fr)

        fr = FileReader(tmp_save_path)

        self.assertEqual([i for i in fr], ['One, two, three shows how', 'Serial commas are good', 'Correcting grammar'])

        fw.delete()

if __name__ == '__main__':
    unittest.main()
