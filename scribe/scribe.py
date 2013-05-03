# coding: utf-8
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
            name = fn.__name__
            if name not in self._cache:
                self._cache[name] = fn(*args, **kwargs)
            return self._cache[name]
        return wrapped

    def get_datafile(self, file):
        return open(path.join(self.path, file))


class IVScribe(Scribe):

    @Scribe.cached
    def get_base_stats(self):
        pass
