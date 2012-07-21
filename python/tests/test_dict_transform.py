import unittest

from sanio.transformers import DictTransform, NonSparseDictTransform
from sanio.readers import ListReader


class TestDictTransform(unittest.TestCase):
    def test_a(self):
        parser = DictTransform(data_source=ListReader([{'foo': 1, 'blah': 2}]), remap_fields={'foo': 'bar'})
        self.assertEqual([i['bar'] for i in parser], [1])

    def test_b(self):
        parser = DictTransform(data_source=ListReader([{'foo': 1, 'blah': 2}]), remap_fields={'foo': 'bar'})
        self.assertEqual([i for i in parser], [{'blah': 2, 'bar': 1}])

    def test_c(self):
        parser = DictTransform(data_source=ListReader([{'foo': 1, 'blah': ''}]), remap_fields={'foo': 'bar'})
        self.assertEqual([i for i in parser], [{'blah': '', 'bar': 1}])


class TestNonSparseDictTransform(unittest.TestCase):
    def test_a(self):
        parser = NonSparseDictTransform(data_source=ListReader([{'foo': 1, 'blah': ''}]), remap_fields={'foo': 'bar'})
        self.assertEqual([i for i in parser], [{'bar': 1}])


## ---------------------
if __name__ == "__main__":
    unittest.main()
