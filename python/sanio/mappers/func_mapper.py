import inspect

from sanio.base import BaseSanio


class FuncMapper(BaseSanio):
    def __init__(self, fn=None, *args, **kwargs):
        self.fn = fn

        super(FuncMapper, self).__init__(*args, **kwargs)

    def clean(self, key=None, value=None):
        result = value

        if self.cleaner is not None:
            try:
                if inspect.ismethod(self.cleaner) or inspect.isfunction(self.cleaner):
                    arg_count = len(inspect.getargspec(self.cleaner)[0])

                    if arg_count == 1:
                        result = self.cleaner(result)

                    elif arg_count == 2:
                        result = self.cleaner(key, result)

                else:
                    result = self.cleaner.clean(key, result)

            except AttributeError:
                # self.cleaner is probably None
                pass

            except TypeError:
                # self.cleaner.clean isn't callable
                pass

        try:
            result = self.fn(value)

        except TypeError:
            pass

        return result
