Cases
-----
Cases is a test cases generation tool.

Possible options:
    - "each choice" cases
    - "pairwise" cases
    - "negative" cases

Installation
------------
Install with pip::

    pip install cases

Install with setup.py::

    python setup.py install

Example
-------
.. code-block:: python

    from cases import Cases

    cases = Cases()

    each_choice_cases = cases.get_each_choice(
        username = ('adaline', 'keegan'),
        gender = ('male', 'female'),
        age = (1, 17, 18, 122) # 122 - oldest person by Guinness World Records
    )

    for case in each_choice_cases:
        print(case.username, case.gender, case.age)

    # ('adaline', 'male', 1)
    # ('keegan', 'female', 17)
    # ('adaline', 'male', 18)
    # ('adaline', 'male', 122)
