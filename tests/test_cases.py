# -*- coding: utf-8 -*-
import string

import pytest
from cases import Cases


@pytest.fixture
def cases():
    return Cases()


@pytest.fixture
def mix(cases):
    return cases.get_mix_gen(string.ascii_letters)


def test_get_one(cases, mix):
    # given
    username = mix(5)
    gender = 'female'
    age = 17
    # when
    case = cases.get_one(
        username=username,
        gender=gender,
        age=age
    )
    # then
    assert case.username == username
    assert case.gender == gender
    assert case.age == age


def test_each_choice(cases, mix):
    # given
    username1, username2 = (mix(1), mix(64))
    gender = 'male'
    age1, age2, age3 = (1, 17, 18)
    # when
    cases = cases.get_each_choice(
        username=(username1, username2),
        gender=(gender,),
        age=(age1, age2, age3)
    )
    # and
    cases = list(cases)
    # then
    assert cases[0].username == username1
    assert cases[0].gender == gender
    assert cases[0].age == age1
    # and
    assert cases[1].username == username2
    assert cases[1].gender == gender
    assert cases[1].age == age2
    # and
    assert cases[2].username == username1
    assert cases[2].gender == gender
    assert cases[2].age == age3
