#
# ~/projects/python/stariter/Makefile ---
#
# $Id: Makefile,v 1.1 2011/01/31 20:22:24 harley Exp $
#


_test: _test_1 _test_2

_test_1:
	python -c "import StarIter"

_test_2:
	./test-stariter
