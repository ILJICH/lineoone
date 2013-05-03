# coding: utf-8
import csv
from os import path

__author__ = 'iljich'

"""
Working with data.
"""


class Scribe(object):

    _cache = {}

    path = 'data'

    def cached(self, fn):
        def wrapped(*args, **kwargs):
            name = repr((fn.__name__, args, kwargs))
            if name not in self._cache:
                self._cache[name] = fn(*args, **kwargs)
            return self._cache[name]
        return wrapped

    def get_data(self, file, vendor=None):
        vendor_path = path.join('vendor', vendor) if vendor else ''
        with open(path.join(self.path, vendor_path, file)) as f:
            reader = csv.reader(f)
            header, data = reader.next(), list(reader)
        return header, data


class IVScribe(Scribe):

    @Scribe.cached
    def get_base_stats(self):
        header, stats = self.get_data('csv/pokemon_stats.csv', vendor='veekun')
        assert header == ['pokemon_id', 'stat_id', 'base_stat', 'effort']

        result = {}
        for pokemon_id, _, stat, _ in stats:
            if pokemon_id not in result:
                result[pokemon_id] = []
            result[pokemon_id].append(stat)

        return result
