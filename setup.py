# -*- coding:utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='cases',
    version='0.1',
    description='Test cases generation tool',
    author='Pavel Vetokhin',
    url='https://github.com/pavetok/cases',
    packages=find_packages(),
    license='MIT License',
    long_description=open('README.md').read(),
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
        'Natural Language :: Russian',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities'
    ]
)