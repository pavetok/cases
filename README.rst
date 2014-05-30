Cases
-----
Cases is a test cases generation tool.

Possible options:
    - "each choice" cases
    - "pairwise" cases
    - "negative" cases

Installation
------------
Install with pip: ::

    pip install cases

Install with setup.py: ::

    python setup.py install

Example
-------
::

    from cases import Cases

    cases = Cases()

    each_choice_cases = cases.each_choice_cases_gen(
        username = ('adaline', 'keegan'),
        gender = ('male', 'female'),
        age = (1, 17, 18, 122) # 122 - oldest person by Guinness World Records
    )

    for case in each_choice_cases:
        print(case.username, case.gender, case.age)

    # ('adaline', 'male', 1)
    # ('keegan', 'female', 17)
    # ('keegan', 'male', 18)
    # ('keegan', 'male', 122)
