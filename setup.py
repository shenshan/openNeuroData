#!/usr/bin/env python
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='one',
    version='0.0.0',
    description='Open neuro data',
    author='ibl',
    author_email='',
    packages=find_packages(exclude=[]),
)