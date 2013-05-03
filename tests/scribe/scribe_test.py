# coding: utf-8
from os import unlink
from tempfile import mkstemp
from unittest import TestCase
import mock

from scribe.scribe import Scribe, IVScribe

__author__ = 'iljich'


def _patch_get_data(header, data):
    def patched(*args, **kwargs):
        return header, data
    return patched


class ScribeTest(TestCase):

    def test_cached(self):
        a = 5

        @Scribe.cached
        def test_0():
            return a

        self.assertEqual(test_0(), 5)
        a = 10
        # It's cached -- it won't change.
        self.assertEqual(test_0(), 5)

        @Scribe.cached
        def test_1(b):
            return b

        self.assertEqual(test_1(5), 5)
        # Arguments are taken in count.
        self.assertEqual(test_1(10), 10)

    def test_get_data(self):
        _, filename = mkstemp()

        with open(filename, 'w') as f:
            f.write('a,b,c\n1,2,3\n4,5,6')

        s = Scribe()
        s.path = '/'
        header, data = s.get_data(filename)
        self.assertEqual(header, ['a', 'b', 'c'])
        self.assertEqual(data, [['1', '2', '3'], ['4', '5', '6']])

        unlink(filename)


class IVCalcTest(TestCase):

    @mock.patch.multiple('scribe.scribe.Scribe', get_data=_patch_get_data(
        ['pokemon_id', 'stat_id', 'base_stat', 'effort'],
        [[1, 1, 45, 0],
         [1, 2, 49, 0],
         [1, 3, 49, 0],
         [1, 4, 65, 1],
         [1, 5, 65, 0],
         [1, 6, 45, 0]]
    ))
    def test_get_base_stat(self):
        s = IVScribe()
        stats = s.get_base_stats()
        self.assertEqual(stats, {1: {1: 45,
                                     2: 49,
                                     3: 49,
                                     4: 65,
                                     5: 65,
                                     6: 45}})

    @mock.patch.multiple('scribe.scribe.Scribe', get_data=_patch_get_data(
        ['nature_id', 'local_language_id', 'name'],
        [[1, 1, 'xHardy'],
         [1, 2, 'xHardy'],
         [1, 3, 'xHardy'],
         [3, 4, 'xHardy'],
         [1, 9, 'Hardy'],
         [2, 9, 'Lonely']]
    ))
    def test_get_nature_names(self):
        s = IVScribe()
        names = s.get_nature_names()
        self.assertEqual(names, {1: 'Hardy', 2: 'Lonely'})

    @mock.patch.multiple('scribe.scribe.Scribe', get_data=_patch_get_data(
        ['id', 'identifier', 'decreased_stat_id', 'increased_stat_id',
         'hates_flavor_id', 'likes_flavor_id'],
        [[1, 'hardy', 2, 2, 1, 1],
         [2, 'bold', 2, 3, 1, 5],
         [3, 'modest', 2, 4, 1, 2]]
    ))
    def test_get_natures(self):
        s = IVScribe()
        names = s.get_natures()
        self.assertEqual(names, {1: (2, 2),
                                 2: (3, 2),
                                 3: (4, 2)})
