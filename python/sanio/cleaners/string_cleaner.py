import re

from sanio.base import BaseSanio


class StringCleaner(BaseSanio):
    @classmethod
    def compress_whitespace(cls, s):
        """
        Convert whitespace (ie., spaces, tabs, linebreaks, etc.) to spaces, and
        compress multiple-spaces into single-spaces.
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
        """
        return ("%s" % (html)).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace("'", '&#39;')

    @classmethod
    def extract_numbers_safe(cls, s, decimals=False):
        """
        Returns a string containing only the numbers from the input string, s.
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
    def initial_caps(cls, s):
        return ' '.join([foo.capitalize() for foo in str(s).split(' ')])

    @classmethod
    def int_or_zero(cls, i):
        return StringCleaner.safe_int(i, default=0)

    @classmethod
    def join(cls, s, key):
        return s.join(key)

    @classmethod
    def lower(cls, s):
        return str(s).lower()

    @classmethod
    def lstrip(cls, s):
        return s.lstrip()

    @classmethod
    def price_like(cls, s):
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
        try:
            return float(cls.price_like(s))

        except ValueError:
            return None

    @classmethod
    def replace(cls, s, key, value):
        return s.replace(key, value)

    @classmethod
    def reverse(cls, s):
        return s[::-1]

    @classmethod
    def remove_null_bytes(cls, s):
        return s.replace('\x00', '')

    @classmethod
    def rstrip(cls, s):
        return s.rstrip()

    @classmethod
    def safe_bool(cls, input):
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
        try:
            return int(arg)
        except:
            try:
                return int(cls.extract_numbers_safe(arg))
            except ValueError:
                return default

    @classmethod
    def safe_split(cls, input, delimiter='_'):
        return cls.escape(input).split(delimiter)

    @classmethod
    def slugify(cls, s):
        if s is None:
            return s

        value = re.sub('[^\w\s-]', '', str(s)).strip().lower()
        value = re.sub('[-\s]+', '-', value)
        value = re.sub('[_\s]+', '-', value)
        return value

    @classmethod
    def sql_safe(cls, s):
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
        """
        if value == None:
            return None

        s = re.sub(r'<\/?p>', ' ', '%s' % value)
        s = re.sub(r'<[^>]*?>', '', s)
        return cls.compress_whitespace(s)

    @classmethod
    def strip_trailing_zeros(cls, s):
        """
        Return the string with and trailing zeros (and trailing decimal points) removed.
        """
        # Make sure there's a '.' in the string.
        if s.find('.') < 0:
            return s

        # Reverse the string, then walk until we find a non-zero.
        rev_str = StringCleaner.reverse(s)

        last_index = -1
        count = -1

        for i in rev_str:
            count += 1

            if i == '0':
                continue
            else:
                last_index = count
                break

        # Slice-off the zeros, re-reverse the string, and strip any trailing '.'s.
        return StringCleaner.reverse(rev_str[last_index:]).rstrip('\.')

    @classmethod
    def super_flat(cls, s):
        """
        Like an upper-case slug with no hyphens.
        """
        if s is None:
            return ''

        return cls.sql_safe(cls.slugify(s).upper().replace('-', ''))

    @classmethod
    def upper(cls, s):
        return str(s).upper()
