#!/usr/bin/env python

import os.path
import setuptools

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as f:
    long_description = f.read()

setuptools.setup(
    name='jhg-python-stariter',
    version='0.1',
    description='Multiple iterators in one.',
    long_description=long_description,
    author='Harley Gorrell',
    author_email='harley@panix.com',
    install_requires=[],
    license='MIT',
    packages=['lib/stariter'],
    url='https://github.com/jhgorrell/jhg-python-stariter',
)
