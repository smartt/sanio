from sanio.base_sanio import BaseSanio


class DictTransform(BaseSanio):
    def __init__(self, *args, **kwargs):
        self.remap_fields = None

        super(DictTransform, self).__init__(*args, **kwargs)

    def __getitem__(self, i):
        # Here's the worst implementation first:
        c = 0
        result = None

        while c <= i:
            try:
                result = self.next()
            except StopIteration:
                break
            else:
                c += 1

        return result

    def next_generator(self):
        for bit in self.data_source:
            yield bit

    def next(self):
        if self._reader_generator is None:
            self._reader_generator = self.next_generator()

        # Grab the next bit of data from the reader, and split it using our
        # frame definitions.
        d = self._reader_generator.next()

        if self.remap_fields is not None:
            results = dict()

            for k, v in d.items():
                try:
                    results[self.remap_fields[k]] = v

                except AttributeError:
                    # self.cleaner is probably None
                    results[k] = v

                except KeyError:
                    # self.remap_fields might not have this key. No problem.
                    results[k] = v

                except TypeError:
                    # self.cleaner.clean isn't callable
                    results[k] = v

            return results

        else:
            return d


class NonSparseDictTransform(DictTransform):
    def __init__(self, *args, **kwargs):
        self.remap_fields = None

        super(NonSparseDictTransform, self).__init__(*args, **kwargs)

    def next(self):
        if self._reader_generator is None:
            self._reader_generator = self.next_generator()

        # Grab the next bit of data from the reader, and split it using our
        # frame definitions.
        d = self._reader_generator.next()
        results = dict()

        for k, v in d.items():
            if (v is not None) and (v is not ''):
                results[k] = v

        if self.remap_fields is not None:
            remap_results = dict()

            for k, v in results.items():
                try:
                    remap_results[self.remap_fields[k]] = v

                except AttributeError:
                    # self.cleaner is probably None
                    remap_results[k] = v

                except KeyError:
                    # self.remap_fields might not have this key. No problem.
                    remap_results[k] = v

                except TypeError:
                    # self.cleaner.clean isn't callable
                    remap_results[k] = v

            results = remap_results

        return results
