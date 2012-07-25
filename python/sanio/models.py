

class SanioField(object):
    def __init__(self, verbose_name=None, name=None, default=None, max_length=None,
            blank=False, null=False, editable=True, choices=None, help_text='',
            validators=[]):
        self.name = name
        self.verbose_name = verbose_name
        self.max_length = max_length
        self.blank = blank
        self.null = null
        self.default = default
        self.editable = editable
        self._choices = choices
        self.help_text = help_text
        self.validators = validators


class BooleanField(SanioField):
    def __init__(self, *args, **kwargs):
        super(BooleanField, self).__init__(*args, **kwargs)


class IntegerField(SanioField):
    def __init__(self, *args, **kwargs):
        super(IntegerField, self).__init__(*args, **kwargs)


class DateField(SanioField):
    def __init__(self, *args, **kwargs):
        super(DateField, self).__init__(*args, **kwargs)


class DateTimeField(SanioField):
    def __init__(self, *args, **kwargs):
        super(DateTimeField, self).__init__(*args, **kwargs)


class DecimalField(SanioField):
    def __init__(self, *args, **kwargs):
        super(DecimalField, self).__init__(*args, **kwargs)


class EmailField(SanioField):
    def __init__(self, *args, **kwargs):
        super(EmailField, self).__init__(*args, **kwargs)


class StringField(SanioField):
    def __init__(self, *args, **kwargs):
        super(StringField, self).__init__(*args, **kwargs)
