from datetime import date
import unittest

from sanio.cleaners import DateTimeCleaner


class TestDateTimeCleaner(unittest.TestCase):

    def test_extract_date_by_pattern(self):
        self.assertEqual(DateTimeCleaner.extract_date_by_pattern('4/20/2014', '%m/%d/%Y'), date(2014, 4, 20))
        self.assertEqual(DateTimeCleaner.extract_date_by_pattern('4/20', '%m/%d'), date(2014, 4, 20))
        self.assertEqual(DateTimeCleaner.extract_date_by_pattern('4.20', '%m.%d'), date(2014, 4, 20))
        self.assertEqual(DateTimeCleaner.extract_date_by_pattern('420', '%m/%d'), None)

## ---------------------
if __name__ == "__main__":
    unittest.main()
