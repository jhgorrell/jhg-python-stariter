#
# jhg-python-stariter/Makefile ---
#

_default: _test

SHELL=bash

###

_ve:
	virtualenv ve
	./ve/bin/pip install autopep8

ve:
	make _ve
###

_autopep8:
	autopep8 -i lib/stariter/*.py

###

_test_unittests:
	python -m unittest discover --start-directory lib --pattern "test_*.py"

_test: ve _test_unittests
