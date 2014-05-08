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
    username = (empty, valid_mix(65), illegal_username, {'default': valid_mix(5)}),
    gender = ('bla', {'default': 'male'}),
    age = (0, 123,  {'default': 25})
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


# --------------------------------------------------
# {'username': 'F', 'gender': 'male', 'age': 1}
# {'username': 'JDGxIRYvGyCmDdljxMQXNsXhtRMFevMFNrbHmNGEdSFhJiFeLVdMEzZiMuSPUigs', 'gender': 'female', 'age': 17}
# {'username': 'JDGxIRYvGyCmDdljxMQXNsXhtRMFevMFNrbHmNGEdSFhJiFeLVdMEzZiMuSPUigs', 'gender': 'male', 'age': 18}
# {'username': 'JDGxIRYvGyCmDdljxMQXNsXhtRMFevMFNrbHmNGEdSFhJiFeLVdMEzZiMuSPUigs', 'gender': 'male', 'age': 122}
# --------------------------------------------------
# {'username': '3', 'gender': 'male', 'age': 0.5}
# {'username': '5153546679344293017936217513851266196118827467042001853312838713', 'gender': 'female', 'age': 0.5}
# {'username': '5153546679344293017936217513851266196118827467042001853312838713', 'gender': 'male', 'age': 17}
# {'username': '3', 'gender': 'female', 'age': 17}
# {'username': '3', 'gender': 'female', 'age': 18}
# {'username': '5153546679344293017936217513851266196118827467042001853312838713', 'gender': 'male', 'age': 18}
# {'username': '5153546679344293017936217513851266196118827467042001853312838713', 'gender': 'male', 'age': 122}
# {'username': '3', 'gender': 'female', 'age': 122}
# --------------------------------------------------
# {'username': '', 'gender': {'default': 'male'}, 'age': {'default': 25}}
# {'username': 'lxiCPWhyIjTzpTuxCPUpnoBItObSHDrxgzJKxCZzowYFUFnZtdYtRmLSgWDmowtDx', 'gender': {'default': 'male'}, 'age': {'default': 25}}
# {'username': 'L?R', 'gender': {'default': 'male'}, 'age': {'default': 25}}
# {'username': {'default': 'aVCyn'}, 'gender': 'bla', 'age': {'default': 25}}
# {'username': {'default': 'aVCyn'}, 'gender': {'default': 'male'}, 'age': 0}
# {'username': {'default': 'aVCyn'}, 'gender': {'default': 'male'}, 'age': 123}

