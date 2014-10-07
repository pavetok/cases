# -*- coding:utf-8 -*-
from setuptools import setup, find_packages


__version__ = '0.1.13'


with open('README.rst') as f:
    long_description = f.read()


setup(
    name='cases',
    version=__version__,
    description='Test cases generation tool',
    author='Pavel Vetokhin',
    url='https://github.com/pavetok/cases',
    packages=find_packages(),
    license='MIT License',
    long_description=long_description,
    install_requires = [
        'AllPairs==2.0.1'
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities'
    ]
)

# python setup.py sdist upload
