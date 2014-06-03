# -*- coding: utf-8 -*-
from metacomm.combinatorics.all_pairs2 import all_pairs2 as allpairs
from itertools import izip, izip_longest
import random
import json


class Case(object):
    def __repr__(self):
        return json.dumps(self.__dict__)


class Cases(object):

    def __init__(self):
        self.CasesClass = Case

    def set_cases_class(self, cls):
        self.CasesClass = cls

    def get_each_choice(self, **kwargs):
        """Returns a generator that generates positive cases by
        "each choice" algorithm.
        """
        defaults = {attr: random.choice(kwargs[attr]) for attr in kwargs}
        for set_of_values in izip_longest(*kwargs.values()):
            case = self.CasesClass()
            for attr, value in izip(kwargs.keys(), set_of_values):
                if value is None:
                    value = defaults[attr]
                setattr(case, attr, value)
            yield case

    def get_pairwise(self, **kwargs):
        """Returns a generator that generates positive cases by
        "pairwise" algorithm.
        """
        for set_of_values in allpairs(kwargs.values()):
            case = self.CasesClass()
            for attr, value in izip(kwargs.keys(), set_of_values):
                setattr(case, attr, value)
            yield case

    def get_negative(self, **kwargs):
        """Returns a generator that generates negative cases by
        "each negative value in separate case" algorithm.
        """
        for attr, set_of_values in kwargs.iteritems():
            defaults = {key: kwargs[key][-1]['default'] for key in kwargs}
            defaults.pop(attr)
            for value in set_of_values[:-1]:
                case = self.CasesClass()
                setattr(case, attr, value)
                for key in defaults:
                    setattr(case, key, defaults[key])
                yield case

    def mix_gen(self, sample):
        """Returns function that returns sequence of characters of a
        given length from a given sample
        """
        def mix(length):
            return ''.join(unicode(random.choice(list(sample))) for _ in xrange(length))
        return mix