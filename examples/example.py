# -*- coding: utf-8 -*-
from cases import Cases
import string


cases = Cases()


mix = cases.get_mix_gen(string.ascii_letters)
one_case = cases.get_one(
    username = mix(5),
    gender = 'female',
    age = 17
)

mix = cases.get_mix_gen(string.ascii_letters)
each_choice_cases = cases.get_each_choice(
    username = (mix(1), mix(64)),
    gender = ('male', 'female'),
    age = (1, 17, 18, 122) # 122 - oldest person by Guinness World Records
)


mix = cases.get_mix_gen(string.digits)
pairwise_cases = cases.get_pairwise(
    username = (mix(1), mix(64)),
    gender = ('male', 'female'),
    age = (0.5, 17, 18, 122) # 122 - oldest person by Guinness World Records
)


empty = ''
valid_mix = cases.get_mix_gen(string.ascii_letters)
invalid_mix = cases.get_mix_gen(string.punctuation)
illegal_username = valid_mix(1) + invalid_mix(1) + valid_mix(1)
negative_cases = cases.get_negative(
    username = (empty, valid_mix(65), illegal_username, {'default': valid_mix(5)}),
    gender = ('bla', {'default': 'male'}),
    age = (0, 123,  {'default': 25})
)


print('-'*50)
print(one_case.__dict__)

print('-'*50)
for case in each_choice_cases:
    print(case.__dict__)

print('-'*50)
for case in pairwise_cases:
    print(case.__dict__)

print('-'*50)
for case in negative_cases:
    print(case.__dict__)


# --------------------------------------------------
# {'username': u'wmDGe', 'gender': 'female', 'age': 17}
# --------------------------------------------------
# {'username': u'p', 'gender': 'male', 'age': 1}
# {'username': u'eJwrOcLhtZTPpAFhxqDLeLPFdqTQdbZAZtvZKTQYlKKwUSHYKigzBHSssYyphikf', 'gender': 'female', 'age': 17}
# {'username': u'p', 'gender': 'male', 'age': 18}
# {'username': u'p', 'gender': 'male', 'age': 122}
# --------------------------------------------------
# {'username': u'3', 'gender': 'male', 'age': 0.5}
# {'username': u'5616725912969705976207092160681081090046202769052624891306304454', 'gender': 'female', 'age': 0.5}
# {'username': u'5616725912969705976207092160681081090046202769052624891306304454', 'gender': 'male', 'age': 17}
# {'username': u'3', 'gender': 'female', 'age': 17}
# {'username': u'3', 'gender': 'female', 'age': 18}
# {'username': u'5616725912969705976207092160681081090046202769052624891306304454', 'gender': 'male', 'age': 18}
# {'username': u'5616725912969705976207092160681081090046202769052624891306304454', 'gender': 'male', 'age': 122}
# {'username': u'3', 'gender': 'female', 'age': 122}
# --------------------------------------------------
# {'username': '', 'gender': 'male', 'age': 25}
# {'username': u'gsdQnfCulFhPZDoVGMpkYAijWvNeMpSMXThhcnYlfAehgNzSVZPudAsyWLJHAQzQI', 'gender': 'male', 'age': 25}
# {'username': u'z,O', 'gender': 'male', 'age': 25}
# {'username': u'sDLMT', 'gender': 'bla', 'age': 25}
# {'username': u'sDLMT', 'gender': 'male', 'age': 0}
# {'username': u'sDLMT', 'gender': 'male', 'age': 123}

