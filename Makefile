#
# jhg-python-stariter/Makefile ---
#

_default: _test

SHELL=bash

###

_ve:
	virtualenv ve

ve:
	make _ve

###

_test_unittests:
	python -m unittest discover --start-directory lib --pattern "test_*.py"

_test: _test_unittests
