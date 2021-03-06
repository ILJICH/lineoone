# coding: utf-8
"""
Working with data.
"""

import csv
from os import path

__author__ = 'iljich'


class Scribe(object):

    _cache = {}

    path = 'data'

    @classmethod
    def cached(cls, fn):
        def wrapped(*args, **kwargs):
            name = repr((fn.__name__, args, kwargs))
            if name not in cls._cache:
                cls._cache[name] = fn(*args, **kwargs)
            return cls._cache[name]
        return wrapped

    def get_data(self, file_, vendor=None):
        vendor_path = path.join('vendor', vendor) if vendor else ''
        with open(path.join(self.path, vendor_path, file_)) as f:
            reader = csv.reader(f)
            header, data = reader.next(), list(reader)
        return header, data


class IVScribe(Scribe):

    @Scribe.cached
    def get_base_stats(self):
        header, stats = self.get_data('csv/pokemon_stats.csv', vendor='veekun')
        assert header == ['pokemon_id', 'stat_id', 'base_stat', 'effort']

        result = {}
        for pokemon_id, stat_id, stat, _ in stats:
            if pokemon_id not in result:
                result[pokemon_id] = {}
            result[int(pokemon_id)][int(stat_id)] = int(stat)
        return result

    @Scribe.cached
    def get_nature_names(self):
        header, names = self.get_data('csv/nature_names.csv', vendor='veekun')
        assert header == ['nature_id', 'local_language_id', 'name']

        language_id = 9
        result = {}
        for nature_id, local_language_id, name in names:
            if int(local_language_id) is language_id:
                result[int(nature_id)] = name
        return result

    def get_natures(self):
        header, natures = self.get_data('csv/natures.csv', vendor='veekun')
        assert header == ['id', 'identifier', 'decreased_stat_id',
                          'increased_stat_id', 'hates_flavor_id',
                          'likes_flavor_id']

        result = {}
        for nature_id, _, dec, inc, _, _ in natures:
            result[int(nature_id)] = (int(inc), int(dec))
        return result
