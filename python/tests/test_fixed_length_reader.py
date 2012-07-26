import unittest

from sanio.cleaners import StringCleaner, FuncCleaner, FuncDictCleaner
from sanio.readers import FileReader, StringReader, FixedLengthReader


class TestFixedLengthReader(unittest.TestCase):
    def test_a(self):
        parser = FixedLengthReader(
            data_source=StringReader('onetwothree'),
            frame_definitions=(('a', 3), ('b', 3), ('c', 5))
        )

        self.assertEqual(
            [i for i in parser],
            [{'a': 'one', 'c': 'three', 'b': 'two'}]
        )

    def test_b(self):
        parser = FixedLengthReader(
            data_source=FileReader('test_data/simple.txt'),
            frame_definitions=(('area', 3), ('base', 3), ('ext', 4))
        )

        self.assertEqual(
            [i for i in parser],
            [{'ext': '4567', 'base': '123', 'area': '555'}, {'ext': '5309', 'base': '867', 'area': '555'}, {'ext': '6543', 'base': '987', 'area': '555'}]
        )

    def test_c(self):
        parser = FixedLengthReader(
            data_source=FileReader('test_data/simple.txt'),
            frame_definitions=(('area', 3), ('base', 3), ('ext', 4)),
            cleaner=FuncCleaner(StringCleaner.safe_int)
        )

        self.assertEqual(
            [i for i in parser],
            [{'ext': 4567, 'base': 123, 'area': 555}, {'ext': 5309, 'base': 867, 'area': 555}, {'ext': 6543, 'base': 987, 'area': 555}]
        )

    def test_d(self):
        parser = FixedLengthReader(
            data_source=FileReader('test_data/simple.txt'),
            frame_definitions=(('area', 3), ('base', 3), ('ext', 4)),
            cleaner=FuncDictCleaner({'ext': StringCleaner.safe_int})
        )

        self.assertEqual(
            [i for i in parser],
            [{'ext': 4567, 'base': '123', 'area': '555'}, {'ext': 5309, 'base': '867', 'area': '555'}, {'ext': 6543, 'base': '987', 'area': '555'}]
        )

if __name__ == '__main__':
    unittest.main()
