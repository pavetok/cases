# -*- coding: utf-8 -*-
from cases import get_each_choice_cases, get_pairwise_cases, \
    get_negative_cases, mixgen
import string


mix = mixgen(string.ascii_letters)
each_choice_cases = get_each_choice_cases(
    username = (mix(1), mix(64)),
    gender = ('male', 'female'),
    age = (1, 17, 18, 122) # 122 - oldest person by Guinness World Records
)


mix = mixgen(string.digits)
pairwise_cases = get_pairwise_cases(
    username = (mix(1), mix(64)),
    gender = ('male', 'female'),
    age = (0.5, 17, 18, 122) # 122 - oldest person by Guinness World Records
)


empty = ''
valid_mix = mixgen(string.ascii_letters)
invalid_mix = mixgen(string.punctuation)
illegal_username = valid_mix(1) + invalid_mix(1) + valid_mix(1)
negative_cases = get_negative_cases(
    username = (empty, valid_mix(65), illegal_username, valid_mix(5)),
    gender = ('bla', 'male'),
    age = (0, 123, 25)
)


print('-'*50)
for case in each_choice_cases:
    print(case.__dict__)

print('-'*50)
for case in pairwise_cases:
    print(case.__dict__)

print('-'*50)
for case in negative_cases:
    print(case.__dict__)

