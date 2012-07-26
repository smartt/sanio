

class BaseField(object):
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


class BooleanField(BaseField):
    def __init__(self, *args, **kwargs):
        super(BooleanField, self).__init__(*args, **kwargs)


class IntegerField(BaseField):
    def __init__(self, *args, **kwargs):
        super(IntegerField, self).__init__(*args, **kwargs)


class DateField(BaseField):
    def __init__(self, *args, **kwargs):
        super(DateField, self).__init__(*args, **kwargs)


class DateTimeField(BaseField):
    def __init__(self, *args, **kwargs):
        super(DateTimeField, self).__init__(*args, **kwargs)


class DecimalField(BaseField):
    def __init__(self, *args, **kwargs):
        super(DecimalField, self).__init__(*args, **kwargs)


class DictField(BaseField):
    def __init__(self, *args, **kwargs):
        super(DictField, self).__init__(*args, **kwargs)


class EmailField(BaseField):
    def __init__(self, *args, **kwargs):
        super(EmailField, self).__init__(*args, **kwargs)


class FunctionField(BaseField):
    def __init__(self, *args, **kwargs):
        super(FunctionField, self).__init__(*args, **kwargs)


class ObjectField(BaseField):
    def __init__(self, *args, **kwargs):
        super(ObjectField, self).__init__(*args, **kwargs)


class StringField(BaseField):
    def __init__(self, *args, **kwargs):
        super(StringField, self).__init__(*args, **kwargs)


class TupleField(BaseField):
    def __init__(self, *args, **kwargs):
        super(TupleField, self).__init__(*args, **kwargs)
