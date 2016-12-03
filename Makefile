#
# jhg-python-stariter/Makefile ---
#

_default: _test

export SHELL=bash
#export PYTHONWARNINGS="Unverified HTTPS request"
#export PYTHONWARNINGS="ignore:Unverified HTTPS request"

###

_ve:
	virtualenv ve
	./ve/bin/pip install autopep8

ve:
	make _ve
###

_autopep8:
	autopep8 -i setup.py lib/stariter/*.py

###

_pip_install_local:
	pip install -e .

_pip_install_github:
	pip install -e git+https://github.com/jhgorrell/jhg-python-stariter#egg=jhg-python-stariter

###

_test_unittests:
	python -m unittest discover --start-directory lib --pattern "test_*.py"

_test: ve _test_unittests


_test_pip_install:
	rm -rf ve-test-pip-install build
	virtualenv ve-test-pip-install
	./ve-test-pip-install/bin/pip install --upgrade pip
# using '-e' results in a bad install.
# the path 
#	-./ve-test-pip-install/bin/pip install git+https://github.com/jhgorrell/jhg-python-stariter#egg=jhg-python-stariter
# works
#	-./ve-test-pip-install/bin/pip install .
	-./ve-test-pip-install/bin/pip install -e .
	-./ve-test-pip-install/bin/python -c "import stariter"
#
	-find . -name star\*
	-cat ./ve-test-pip-install/lib/python2.7/site-packages/jhg-python-stariter.egg-link
