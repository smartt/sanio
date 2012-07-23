import unittest

from sanio.cleaners import StringCleaner
from sanio.mappers import FuncMapper, FuncDictMapper
from sanio.readers import CSVReader, FileReader  # , StringReader
from sanio.transformers import DictTransform


class TestCSVReaders(unittest.TestCase):
#     def test_multiline(self):
#         in_data = '''"a","b","c"
# "one","two","3"
# '''
#         parser = CSVReader(data_source=StringReader(in_data))
#         self.assertEqual([i for i in parser], [{'a': 'one', 'b': 'two', 'c': '3'}])

    def test_a(self):
        parser = CSVReader(data_source=FileReader('tests/test_data/simple.csv'))
        self.assertEqual([i for i in parser], [{'a': 'one', 'b': 'two', 'c': '3'}])

    def test_b(self):
        parser = CSVReader(data_source=FileReader('tests/test_data/simple.csv'), cleaner=FuncMapper(StringCleaner.safe_int))
        self.assertEqual([i for i in parser], [{'a': None, 'b': None, 'c': 3}])

    def test_c(self):
        parser = CSVReader(data_source=FileReader('tests/test_data/simple.csv'), cleaner=FuncDictMapper({'c': StringCleaner.safe_int}))
        self.assertEqual([i for i in parser], [{'a': 'one', 'b': 'two', 'c': 3}])

    def test_d(self):
        parser = CSVReader(data_source=FileReader('tests/test_data/simple.csv'), cleaner=FuncDictMapper({'c': StringCleaner.safe_int}))
        self.assertEqual(parser(), [{'a': 'one', 'b': 'two', 'c': 3}])

    def test_e(self):
        parser = CSVReader(data_source=FileReader('tests/test_data/numbers.csv'))
        self.assertEqual([i for i in parser], [{'Volume': '12244871', 'Day Change': '-15.08', 'Price': '587.92', 'High': '598.40', 'SMBL': 'AAPL', 'Low': '584.75', 'Time': '1:54pm', 'Date': '4/30/2012', 'Open': '597.94'}, {'Volume': '1022507', 'Day Change': '-7.09', 'Price': '607.89', 'High': '616.082', 'SMBL': 'GOOG', 'Low': '607.67', 'Time': '1:55pm', 'Date': '4/30/2012', 'Open': '612.99'}, {'Volume': '4504323', 'Day Change': '-3.18', 'Price': '80.56', 'High': '83.8723', 'SMBL': 'NFLX', 'Low': '80.10', 'Time': '1:56pm', 'Date': '4/30/2012', 'Open': '82.61'}])

    def test_f(self):
        parser = CSVReader(data_source=FileReader('tests/test_data/numbers.csv'))
        self.assertEqual([i['SMBL'] for i in parser], ['AAPL', 'GOOG', 'NFLX'])

    def test_g(self):
        parser = DictTransform(data_source=CSVReader(data_source=FileReader('tests/test_data/numbers.csv')), remap_fields={'SMBL': 'Symbol'})
        self.assertEqual([i['Symbol'] for i in parser], ['AAPL', 'GOOG', 'NFLX'])

        self.assertEqual([i['Symbol'] for i in DictTransform(data_source=CSVReader(data_source=FileReader('tests/test_data/numbers.csv')), remap_fields={'SMBL': 'Symbol'})], ['AAPL', 'GOOG', 'NFLX'])

    def test_h(self):
        parser = CSVReader(data_source=FileReader('tests/test_data/numbers.csv'))
        self.assertEqual(parser[0]['SMBL'], 'AAPL')

        self.assertEqual(parser[0]['SMBL'], 'AAPL')

        self.assertEqual(parser[1]['SMBL'], 'GOOG')

    def test_i(self):
        parser = CSVReader(data_source=FileReader('tests/test_data/numbers.csv'))
        self.assertEqual(parser[2]['SMBL'], 'NFLX')

        self.assertEqual(parser[0]['SMBL'], 'AAPL')


## ---------------------
if __name__ == "__main__":
    unittest.main()
