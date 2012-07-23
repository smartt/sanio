import unittest

from sanio.cleaners import StringCleaner


class TestStringCleaner(unittest.TestCase):
    def test_compress_whitespace(self):
        self.assertEqual(StringCleaner.compress_whitespace('   Oh   hai    there   '), 'Oh hai there')
        self.assertEqual(StringCleaner.compress_whitespace('      '), '')

    def test_escape(self):
        self.assertEqual(StringCleaner.escape('<b>oh hai</b>'), '&lt;b&gt;oh hai&lt;/b&gt;')
        self.assertEqual(StringCleaner.escape("Quote's Test"), 'Quote&#39;s Test')

    def test_extract_numbers_safe(self):
        self.assertEqual(StringCleaner.extract_numbers_safe('123'), '123')
        self.assertEqual(StringCleaner.extract_numbers_safe('1a2b3c'), '123')
        self.assertEqual(StringCleaner.extract_numbers_safe('1-2-3-'), '123')
        self.assertEqual(StringCleaner.extract_numbers_safe(None), '')
        self.assertEqual(StringCleaner.extract_numbers_safe(7), '7')
        self.assertEqual(StringCleaner.extract_numbers_safe('-1'), '-1')
        self.assertEqual(StringCleaner.extract_numbers_safe('-3.14'), '-314')
        self.assertEqual(StringCleaner.extract_numbers_safe('-3.14', decimals=True), '-3.14')
        self.assertEqual(StringCleaner.extract_numbers_safe('-314', decimals=True), '-314')
        self.assertEqual(StringCleaner.extract_numbers_safe('314', decimals=True), '314')
        self.assertEqual(StringCleaner.extract_numbers_safe('-3.14.25'), '-31425')
        self.assertEqual(StringCleaner.extract_numbers_safe('-3.14.25', decimals=True), '-3.14')
        self.assertEqual(StringCleaner.extract_numbers_safe('1,024'), '1024')

    def test_initial_caps(self):
        self.assertEqual(StringCleaner.initial_caps('Hi There'), 'Hi There')
        self.assertEqual(StringCleaner.initial_caps('hi there'), 'Hi There')

    def test_lower(self):
        self.assertEqual(StringCleaner.lower('Hi There'), 'hi there')
        self.assertEqual(StringCleaner.lower('hi there'), 'hi there')
        self.assertEqual(StringCleaner.lower('42'), '42')
        self.assertEqual(StringCleaner.lower(42), '42')

    def test_price_like(self):
        self.assertEqual(StringCleaner.price_like(''), '')
        self.assertEqual(StringCleaner.price_like('$19.95'), '19.95')
        self.assertEqual(StringCleaner.price_like('19.95'), '19.95')
        self.assertEqual(StringCleaner.price_like('19.95345'), '19.95')
        self.assertEqual(StringCleaner.price_like('19.5'), '19.50')
        self.assertEqual(StringCleaner.price_like('19.'), '19.00')
        self.assertEqual(StringCleaner.price_like('19'), '19.00')
        self.assertEqual(StringCleaner.price_like('19.5.34'), '')
        self.assertEqual(StringCleaner.price_like('.19'), '0.19')

    def test_price_like_float(self):
        self.assertEqual(StringCleaner.price_like_float(''), None)
        self.assertEqual(StringCleaner.price_like_float('$19.95'), 19.95)
        self.assertEqual(StringCleaner.price_like_float('19.95'), 19.95)
        self.assertEqual(StringCleaner.price_like_float('19.95345'), 19.95)
        self.assertEqual(StringCleaner.price_like_float('19.5'), 19.5)
        self.assertEqual(StringCleaner.price_like_float('19.'), 19.0)
        self.assertEqual(StringCleaner.price_like_float('19'), 19.0)
        self.assertEqual(StringCleaner.price_like_float('19.5.34'), None)
        self.assertEqual(StringCleaner.price_like_float('.19'), 0.19)

    def test_safe_bool(self):
        self.assertTrue(StringCleaner.safe_bool('1'))
        self.assertTrue(StringCleaner.safe_bool('True'))
        self.assertTrue(StringCleaner.safe_bool(True))
        self.assertTrue(StringCleaner.safe_bool('on'))

    def test_not_safe_bool(self):
        self.assertFalse(StringCleaner.safe_bool(False))
        self.assertFalse(StringCleaner.safe_bool('False'))
        self.assertFalse(StringCleaner.safe_bool('0'))
        self.assertFalse(StringCleaner.safe_bool(None))

    def test_safe_int(self):
        self.assertEqual(StringCleaner.safe_int('0'), 0)
        self.assertEqual(StringCleaner.safe_int('1'), 1)
        self.assertEqual(StringCleaner.safe_int('a'), None)
        self.assertEqual(StringCleaner.safe_int('12.3'), 123)
        self.assertEqual(StringCleaner.safe_int('1a2b3c'), 123)
        self.assertEqual(StringCleaner.safe_int('<1a2b3c/>'), 123)
        self.assertEqual(StringCleaner.safe_int(None), None)
        self.assertEqual(StringCleaner.safe_int('None'), None)
        self.assertEqual(StringCleaner.safe_int(1), 1)
        self.assertEqual(StringCleaner.safe_int(u''), None)
        self.assertEqual(StringCleaner.safe_int(1, None), 1)
        self.assertEqual(StringCleaner.safe_int('hi', 0), 0)
        self.assertEqual(StringCleaner.safe_int(None, 0), 0)
        self.assertEqual(StringCleaner.safe_int(None, None), None)
        self.assertEqual(StringCleaner.safe_int(u'', 0), 0)
        self.assertEqual(StringCleaner.safe_int(u'-1'), -1)
        self.assertEqual(StringCleaner.safe_int('0044500'), 44500)

    def test_safe_split(self):
        self.assertEqual(StringCleaner.safe_split('hi_there', '_'), ['hi', 'there'])
        self.assertEqual(StringCleaner.safe_split('<blink>Hai World</blink>', ' '), ['&lt;blink&gt;Hai', 'World&lt;/blink&gt;'])
        self.assertEqual(StringCleaner.safe_split('_', '_'), ['', ''])

    def test_slugify(self):
        self.assertEqual(StringCleaner.slugify('oh hai'), 'oh-hai')
        self.assertEqual(StringCleaner.slugify('OH HAI'), 'oh-hai')
        self.assertEqual(StringCleaner.slugify('"oh_hai!"'), 'oh-hai')
        self.assertEqual(StringCleaner.slugify("oh_hai!'s"), 'oh-hais')

    def test_sql_safe(self):
        self.assertEqual(StringCleaner.sql_safe(None), None)
        self.assertEqual(StringCleaner.sql_safe('hi there'), 'hi there')
        self.assertEqual(StringCleaner.sql_safe('foo/'), 'foo')
        self.assertEqual(StringCleaner.sql_safe('hi -- there'), 'hi   there')
        self.assertEqual(StringCleaner.sql_safe('hi; there'), 'hi there')
        self.assertEqual(StringCleaner.sql_safe("hi' WHERE=1"), "hi\' WHERE=1")
        self.assertEqual(StringCleaner.sql_safe('hi /* there */'), 'hi  there')

    def test_strip_and_compact_str(self):
        self.assertEqual(StringCleaner.strip_and_compact_str('Hi there. <br /><br />Whats up?'), 'Hi there. Whats up?')
        self.assertEqual(StringCleaner.strip_and_compact_str('     Hi         there. <br />    <br />  Whats    up?   '), 'Hi there. Whats up?')
        self.assertEqual(StringCleaner.strip_and_compact_str('\t  Hi \r there. <br /><br />Whats up?'), 'Hi there. Whats up?')
        self.assertEqual(StringCleaner.strip_and_compact_str('<p>Hi there. <br /><br />Whats up?</p>'), 'Hi there. Whats up?')
        self.assertEqual(StringCleaner.strip_and_compact_str("Hi there.  Let's have tea."), "Hi there. Let's have tea.")
        self.assertEqual(StringCleaner.strip_and_compact_str("<i>Hi there.</i><i>Let's have tea."), "Hi there.Let's have tea.")

    def test_strip_tags(self):
        self.assertEqual(StringCleaner.strip_tags('<b>oh hai</b>'), 'oh hai')
        self.assertEqual(StringCleaner.strip_tags(None), None)
        self.assertEqual(StringCleaner.strip_tags('<p>oh hai.</p><p>goodbye</p>'), 'oh hai. goodbye')
        self.assertEqual(StringCleaner.strip_tags('<i>oh hai.</i><i>goodbye</i>'), 'oh hai.goodbye')

    def test_super_flat(self):
        self.assertEqual(StringCleaner.super_flat(''), '')
        self.assertEqual(StringCleaner.super_flat(None), '')
        self.assertEqual(StringCleaner.super_flat('123-456-abc'), '123456ABC')

    def test_upper(self):
        self.assertEqual(StringCleaner.upper('Hi There'), 'HI THERE')
        self.assertEqual(StringCleaner.upper('hi there'), 'HI THERE')
        self.assertEqual(StringCleaner.upper('42'), '42')
        self.assertEqual(StringCleaner.upper(42), '42')


## ---------------------
if __name__ == "__main__":
    unittest.main()
