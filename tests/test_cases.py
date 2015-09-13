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
    age = 17
    # when
    case = cases.get_one(
        username=username,
        age=age
    )
    # then
    assert case.username == username
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
    actuals = list(cases)
    # then
    assert actuals[0].username == username1
    assert actuals[0].gender == gender
    assert actuals[0].age == age1
    # and
    assert actuals[1].username == username2
    assert actuals[1].gender == gender
    assert actuals[1].age == age2
    # and
    assert actuals[2].username == username1
    assert actuals[2].gender == gender
    assert actuals[2].age == age3


def test_pairwise(cases, mix):
    # given
    username1, username2 = (mix(1), mix(64))
    age1, age2, age3 = (1, 17, 18)
    # when
    cases = cases.get_pairwise(
        username=(username1, username2),
        age=(age1, age2, age3)
    )
    # and
    actuals = list(cases)
    # then
    assert len(actuals) == 6
    # and
    assert actuals[0].username == username1
    assert actuals[0].age == age1
    # and
    assert actuals[1].username == username2
    assert actuals[1].age == age1
    # and
    assert actuals[2].username == username2
    assert actuals[2].age == age2
    # and
    assert actuals[3].username == username1
    assert actuals[3].age == age2
    # and
    assert actuals[4].username == username1
    assert actuals[4].age == age3
    # and
    assert actuals[5].username == username2
    assert actuals[5].age == age3


def test_negative(cases, mix):
    # given
    invalid_username, valid_username = (mix(65), mix(10))
    invalid_age1, invalid_age2, valid_age = (0, 1000, 10)
    # when
    cases = cases.get_negative(
        username=(invalid_username, {'default': valid_username}),
        age=(invalid_age1, invalid_age2, {'default': valid_age})
    )
    # and
    actuals = list(cases)
    # then
    assert actuals[0].username == invalid_username
    assert actuals[0].age == valid_age
    # and
    assert actuals[1].username == valid_username
    assert actuals[1].age == invalid_age1
    # and
    assert actuals[2].username == valid_username
    assert actuals[2].age == invalid_age2
