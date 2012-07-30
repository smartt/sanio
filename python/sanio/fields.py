

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

    def __unicode__(self):
        return u"`{n}` {t}".format(n=self.name, t=self.__class__)

    def __repr__(self):
        return self.__unicode__()


class BooleanField(BaseField):
    pass


class IntegerField(BaseField):
    pass


class DateField(BaseField):
    pass


class DateTimeField(BaseField):
    pass


class DecimalField(BaseField):
    pass


class DictField(BaseField):
    pass


class EmailField(BaseField):
    pass


class FunctionField(BaseField):
    pass


class ListField(BaseField):
    pass


class ObjectField(BaseField):
    pass


class StringField(BaseField):
    pass


class TupleField(BaseField):
    pass
