# import inspect

from sanio.base import BaseSanio
from sanio import fields


class FuncMapper(BaseSanio):
    fn = fields.FunctionField(null=True)
    fn_map = fields.DictField(null=True)

    def clean(self, key=None, value=None):
        result = value

        # if self.cleaner is not None:
        #     try:
        #         # Make sure our cleaner is runnable
        #         if inspect.ismethod(self.cleaner) or inspect.isfunction(self.cleaner):
        #             arg_count = len(inspect.getargspec(self.cleaner)[0])

        #             if arg_count == 1:
        #                 result = self.cleaner(result)

        #             elif arg_count == 2:
        #                 result = self.cleaner(key, result)

        #         else:
        #             result = self.cleaner.clean(key, result)

        #     except AttributeError:
        #         # self.cleaner is probably None
        #         pass

        #     except TypeError:
        #         # self.cleaner.clean isn't callable
        #         pass

        if self.fn is not None:
            try:
                result = self.fn(value)

            except TypeError:
                pass

        elif self.fn_map is not None:
            # Support fn_map[key] = func_ptr AND fn_map[key] = [func_prt, func_ptr, ...]
            if key in self.fn_map:
                if isinstance(self.fn_map[key], (list,)):
                    result = value

                    for fn in self.fn_map[key]:
                        result = fn(result)

                elif hasattr(self.fn_map[key], '__call__'):
                    result = self.fn_map[key](value)

        return result
