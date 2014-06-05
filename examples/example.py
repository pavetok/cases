# -*- coding: utf-8 -*-
from cases import Cases
import string


cases = Cases()


mix = cases.mix_gen(string.ascii_letters)
each_choice_cases = cases.get_each_choice(
    username = (mix(1), mix(64)),
    gender = ('male', 'female'),
    age = (1, 17, 18, 122) # 122 - oldest person by Guinness World Records
)


mix = cases.mix_gen(string.digits)
pairwise_cases = cases.get_pairwise(
    username = (mix(1), mix(64)),
    gender = ('male', 'female'),
    age = (0.5, 17, 18, 122) # 122 - oldest person by Guinness World Records
)


empty = ''
valid_mix = cases.mix_gen(string.ascii_letters)
invalid_mix = cases.mix_gen(string.punctuation)
illegal_username = valid_mix(1) + invalid_mix(1) + valid_mix(1)
negative_cases = cases.get_negative(
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
# {'username': u't', 'gender': 'male', 'age': 1}
# {'username': u'qllaBHSVkPwRKtAARqbHNRXaCIbVUygTTJBicHAxqDtLYwUwkNEBjkVFPQWIdcRL', 'gender': 'female', 'age': 17}
# {'username': u't', 'gender': 'male', 'age': 18}
# {'username': u't', 'gender': 'male', 'age': 122}
# --------------------------------------------------
# {'username': u'5', 'gender': 'male', 'age': 0.5}
# {'username': u'5535853260485795223224600570751986899318115935733469903141532756', 'gender': 'female', 'age': 0.5}
# {'username': u'5535853260485795223224600570751986899318115935733469903141532756', 'gender': 'male', 'age': 17}
# {'username': u'5', 'gender': 'female', 'age': 17}
# {'username': u'5', 'gender': 'female', 'age': 18}
# {'username': u'5535853260485795223224600570751986899318115935733469903141532756', 'gender': 'male', 'age': 18}
# {'username': u'5535853260485795223224600570751986899318115935733469903141532756', 'gender': 'male', 'age': 122}
# {'username': u'5', 'gender': 'female', 'age': 122}
# --------------------------------------------------
# {'username': '', 'gender': 'male', 'age': 25}
# {'username': u'wwoYdvcmKEJerTZsaaMJTfYdNyjJmKFkGWopJMUQdQKLPrOmbVBjijLeoLaSGBzJE', 'gender': 'male', 'age': 25}
# {'username': u'm`b', 'gender': 'male', 'age': 25}
# {'username': u'lzRTB', 'gender': 'bla', 'age': 25}
# {'username': u'lzRTB', 'gender': 'male', 'age': 0}
# {'username': u'lzRTB', 'gender': 'male', 'age': 123}

