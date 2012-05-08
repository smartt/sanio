import re

from base_cleaner import BaseCleaner


class StringCleaner(BaseCleaner):
    def __init__(self, *args, **kwargs):
        super(StringCleaner, self).__init__(*args, **kwargs)

    @classmethod
    def compress_whitespace(cls, s):
        """
        Convert whitespace (ie., spaces, tabs, linebreaks, etc.) to spaces, and
        compress multiple-spaces into single-spaces.

        >>> StringCleaner.compress_whitespace('   Oh   hai    there   ')
        'Oh hai there'

        >>> StringCleaner.compress_whitespace('      ')
        ''

        """
        # Cast to string
        s = str(s).strip()

        # Sanity check
        if (len(s) == 0):
            return ''

        s = re.sub(r'\s', ' ', s)
        s = re.sub(r' +', ' ', s)

        return s.strip()

    @classmethod
    def escape(cls, html):
        """
        Returns the given HTML with ampersands, quotes and carets encoded.

        >>> StringCleaner.escape('<b>oh hai</b>')
        '&lt;b&gt;oh hai&lt;/b&gt;'

        >>> StringCleaner.escape("Quote's Test")
        'Quote&#39;s Test'

        """
        return ("%s" % (html)).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace("'", '&#39;')

    @classmethod
    def extract_numbers_safe(cls, s, decimals=False):
        """
        >>> StringCleaner.extract_numbers_safe('123')
        '123'

        >>> StringCleaner.extract_numbers_safe('1a2b3c')
        '123'

        >>> StringCleaner.extract_numbers_safe('1-2-3-')
        '123'

        >>> StringCleaner.extract_numbers_safe(None)
        ''

        >>> StringCleaner.extract_numbers_safe(7)
        '7'

        >>> StringCleaner.extract_numbers_safe('-1')
        '-1'

        >>> StringCleaner.extract_numbers_safe('-3.14')
        '-314'

        >>> StringCleaner.extract_numbers_safe('-3.14', decimals=True)
        '-3.14'

        >>> StringCleaner.extract_numbers_safe('-314', decimals=True)
        '-314'

        >>> StringCleaner.extract_numbers_safe('314', decimals=True)
        '314'

        >>> StringCleaner.extract_numbers_safe('-3.14.25')
        '-31425'

        >>> StringCleaner.extract_numbers_safe('-3.14.25', decimals=True)
        '-3.14'

        >>> StringCleaner.extract_numbers_safe('1,024')
        '1024'

        """
        if decimals:
            tmp = ''.join([i for i in cls.escape(s) if ((i >= '0') and (i <= '9') or i == '.')])

            parts = tmp.split('.')

            try:
                output = '{a}.{b}'.format(a=parts[0], b=parts[1])
            except IndexError:
                output = parts[0]

        else:
            output = ''.join([i for i in cls.escape(s) if (i >= '0') and (i <= '9')])

        try:
            if s[0] == '-':
                output = '-{s}'.format(s=output)
        except:
            pass

        return output

    @classmethod
    def int_or_zero(i):
        return StringCleaner.safe_int(i, default=0)

    @classmethod
    def price_like(cls, s):
        """
        >>> StringCleaner.price_like('')
        ''

        >>> StringCleaner.price_like('$19.95')
        '19.95'

        >>> StringCleaner.price_like('19.95')
        '19.95'

        >>> StringCleaner.price_like('19.95345')
        '19.95'

        >>> StringCleaner.price_like('19.5')
        '19.50'

        >>> StringCleaner.price_like('19.')
        '19.00'

        >>> StringCleaner.price_like('19')
        '19.00'

        >>> StringCleaner.price_like('19.5.34')
        ''

        >>> StringCleaner.price_like('.19')
        '0.19'

        """
        if s.strip() == '':
            return ''

        parts = s.split('.')

        if not len(parts):  # == 0
            # This shouldn't happen. split() should always return at least a one-item list
            return ''

        if len(parts) == 2:
            dollars = cls.extract_numbers_safe(parts[0].strip())
            cents = cls.extract_numbers_safe(parts[1].strip())

        elif len(parts) == 1:
            dollars = cls.extract_numbers_safe(parts[0].strip())
            cents = '00'

        else:
            return ''

        if dollars == '':
            dollars = '0'

        if len(cents) == 2:
            pass

        elif len(cents) > 2:
            # Change '12345' to '12'
            cents = cents[:2]

        elif len(cents) == 1:
            # Chagne '5' to '50'
            cents = '%s0' % cents

        else:
            # Change '' to '00'
            cents = '00'

        return "%s.%s" % (dollars, cents)

    @classmethod
    def price_like_float(cls, s):
        """
        >>> StringCleaner.price_like_float('')


        >>> StringCleaner.price_like_float('$19.95')
        19.949999999999999

        >>> StringCleaner.price_like_float('19.95')
        19.949999999999999

        >>> StringCleaner.price_like_float('19.95345')
        19.949999999999999

        >>> StringCleaner.price_like_float('19.5')
        19.5

        >>> StringCleaner.price_like_float('19.')
        19.0

        >>> StringCleaner.price_like_float('19')
        19.0

        >>> StringCleaner.price_like_float('19.5.34')


        >>> StringCleaner.price_like_float('.19')
        0.19

        """

        try:
            return float(cls.price_like(s))

        except ValueError:
            return

    @classmethod
    def remove_null_bytes(cls, s):
        return s.replace('\x00', '')

    @classmethod
    def safe_bool(cls, input):
        """
        >>> StringCleaner.safe_bool('1')
        True

        >>> StringCleaner.safe_bool('True')
        True

        >>> StringCleaner.safe_bool(True)
        True

        >>> StringCleaner.safe_bool(False)
        False

        >>> StringCleaner.safe_bool('False')
        False

        >>> StringCleaner.safe_bool('0')
        False

        >>> StringCleaner.safe_bool(None)
        False

        >>> StringCleaner.safe_bool('on')
        True

        """
        if input is None:
            return False

        safe_arg = cls.strip_tags(input)

        if safe_arg == u'0' or safe_arg == '0':
            return False

        #if safe_arg == u'on' or safe_arg == 'on':
            #return True

        elif safe_arg == u'False' or safe_arg == 'False':
            return False

        else:
            if bool(safe_arg):
                return True
            else:
                return False

    @classmethod
    def safe_int(cls, arg, default=None):
        """
        >>> StringCleaner.safe_int('0')
        0

        >>> StringCleaner.safe_int('1')
        1

        >>> StringCleaner.safe_int('a')

        >>> StringCleaner.safe_int('12.3')
        123

        >>> StringCleaner.safe_int('1a2b3c')
        123

        >>> StringCleaner.safe_int('<1a2b3c/>')
        123

        >>> StringCleaner.safe_int(None)


        >>> StringCleaner.safe_int('None')


        >>> StringCleaner.safe_int(1)
        1

        >>> StringCleaner.safe_int(u'')


        >>> StringCleaner.safe_int(1, None)
        1

        >>> StringCleaner.safe_int('hi', 0)
        0

        >>> StringCleaner.safe_int(None, 0)
        0

        >>> StringCleaner.safe_int(None, None)


        >>> StringCleaner.safe_int(u'', 0)
        0

        >>> StringCleaner.safe_int(u'-1')
        -1

        >>> StringCleaner.safe_int('0044500')
        44500

        """
        try:
            return int(arg)
        except:
            try:
                return int(cls.extract_numbers_safe(arg))
            except ValueError:
                return default

    @classmethod
    def safe_split(cls, input, delimiter='_'):
        """
        >>> StringCleaner.safe_split('hi_there', '_')
        ['hi', 'there']

        >>> StringCleaner.safe_split('<blink>Hai World</blink>', ' ')
        ['&lt;blink&gt;Hai', 'World&lt;/blink&gt;']

        >>> StringCleaner.safe_split('_', '_')
        ['', '']

        """
        return cls.escape(input).split(delimiter)

    @classmethod
    def slugify(cls, s):
        """
        >>> StringCleaner.slugify('oh hai')
        'oh-hai'

        >>> StringCleaner.slugify('OH HAI')
        'oh-hai'

        >>> StringCleaner.slugify('"oh_hai!"')
        'oh-hai'

        >>> StringCleaner.slugify("oh_hai!'s")
        'oh-hais'
        """
        if s is None:
            return s

        value = re.sub('[^\w\s-]', '', str(s)).strip().lower()
        value = re.sub('[-\s]+', '-', value)
        value = re.sub('[_\s]+', '-', value)
        return value

    @classmethod
    def sql_safe(cls, s):
        """
        >>> StringCleaner.sql_safe(None)


        >>> StringCleaner.sql_safe('hi there')
        'hi there'

        >>> StringCleaner.sql_safe('foo/')
        'foo'

        >>> StringCleaner.sql_safe('hi -- there')
        'hi   there'

        >>> StringCleaner.sql_safe('hi; there')
        'hi there'

        >>> StringCleaner.sql_safe("hi' WHERE=1")
        "hi\' WHERE=1"

        >>> StringCleaner.sql_safe('hi /* there */')
        'hi  there'
        """
        if s is None:
            return None

        s = cls.strip_tags(s).replace(';', '').replace('--', ' ').replace('/', '').replace('*', '').replace('/', '').replace("'", "\'").replace('"', '\"').strip()
        return s

    @classmethod
    def strip(cls, s):
        return s.strip()

    @classmethod
    def strip_and_compact_str(cls, s, append_punctuation=''):
        """
        Remove tags, spaces, etc.  Basically, if someone passed in multiple
        paragraphs, we're going to compact the text into a single block.

        >>> StringCleaner.strip_and_compact_str('Hi there. <br /><br />Whats up?')
        'Hi there. Whats up?'

        >>> StringCleaner.strip_and_compact_str('     Hi         there. <br />    <br />  Whats    up?   ')
        'Hi there. Whats up?'

        >>> StringCleaner.strip_and_compact_str('\t  Hi \r there. <br /><br />Whats up?')
        'Hi there. Whats up?'

        >>> StringCleaner.strip_and_compact_str('<p>Hi there. <br /><br />Whats up?</p>')
        'Hi there. Whats up?'

        >>> StringCleaner.strip_and_compact_str("Hi there.  Let's have tea.")
        "Hi there. Let's have tea."

        >>> StringCleaner.strip_and_compact_str("<i>Hi there.</i><i>Let's have tea.")
        "Hi there.Let's have tea."

        """
        # Strip tabs
        s = cls.strip_tags(s)

        # Compact whitespace
        s = cls.compress_whitespace(s)

        try:
            # Append a trailing append_punctuation if there is none
            if append_punctuation and (s[-1] not in ('.', '!', ')', '?')):
                s = '{s}{a}'.format(s=s, a=append_punctuation)

        except IndexError:
            # Odds are len(s) == 0
            pass

        return s

    @classmethod
    def strip_tags(cls, value):
        """
        Returns the given HTML with all tags stripped.

        >>> StringCleaner.strip_tags('<b>oh hai</b>')
        'oh hai'

        >>> StringCleaner.strip_tags(None)

        >>> StringCleaner.strip_tags('<p>oh hai.</p><p>goodbye</p>')
        'oh hai. goodbye'

        >>> StringCleaner.strip_tags('<i>oh hai.</i><i>goodbye</i>')
        'oh hai.goodbye'

        """
        if value == None:
            return None

        s = re.sub(r'<\/?p>', ' ', '%s' % value)
        s = re.sub(r'<[^>]*?>', '', s)
        return cls.compress_whitespace(s)

    @classmethod
    def super_flat(cls, s):
        """
        >>> StringCleaner.super_flat('')
        ''

        >>> StringCleaner.super_flat(None)
        ''

        >>> StringCleaner.super_flat('123-456-abc')
        '123456ABC'

        """
        if s is None:
            return ''

        return cls.sql_safe(cls.slugify(s).upper().replace('-', ''))

## ---------------------
if __name__ == "__main__":
    import doctest
    print "Testing..."
    doctest.testmod()
    print "Done."
