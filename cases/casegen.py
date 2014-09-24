# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from metacomm.combinatorics.all_pairs2 import all_pairs2 as allpairs
from itertools import izip, izip_longest
import random
import json


class Case(object):
    def __repr__(self):
        return json.dumps({key: value for key, value in self.__dict__.iteritems() \
                           if value is not None})


class Cases(object):

    def __init__(self):
        self._CasesClass = Case

    def set_class(self, cls):
        self._CasesClass = cls

    def set_default(self):
        self._CasesClass = Case

    def get_one(self, **kwargs):
        """Returns a one case."""
        case = self._CasesClass()
        for attr, value in kwargs.iteritems():
            setattr(case, attr, value)
        return case

    def get_each_choice(self, **kwargs):
        """Returns all positive cases by "each choice" algorithm."""
        result = []
        defaults = {attr: kwargs[attr][0] for attr in kwargs}
        for set_of_values in izip_longest(*kwargs.values()):
            case = self._CasesClass()
            for attr, value in izip(kwargs.keys(), set_of_values):
                if value is None:
                    value = defaults[attr]
                setattr(case, attr, value)
            result.append(case)
        return result

    def get_pairwise(self, **kwargs):
        """Returns all positive cases by "pairwise" algorithm."""
        result = []
        for set_of_values in allpairs(kwargs.values()):
            case = self._CasesClass()
            for attr, value in izip(kwargs.keys(), set_of_values):
                setattr(case, attr, value)
            result.append(case)
        return result

    def get_negative(self, **kwargs):
        """Returns all negative cases by "each negative value in separate case" algorithm."""
        result = []
        for attr, set_of_values in kwargs.iteritems():
            defaults = {key: kwargs[key][-1]["default"] for key in kwargs}
            defaults.pop(attr)
            for value in set_of_values[:-1]:
                case = self._CasesClass()
                setattr(case, attr, value)
                for key in defaults:
                    setattr(case, key, defaults[key])
                result.append(case)
        return result

    def get_mix_gen(self, sample):
        """Returns function that returns sequence of characters of a
        given length from a given sample
        """
        def mix(length):
            return "".join(random.choice(sample) for _ in xrange(length))
        return mix