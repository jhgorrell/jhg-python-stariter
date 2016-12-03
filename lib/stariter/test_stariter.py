#
# jhg-python-stariter/lib/stariter/test_stariter.py ---
#

import unittest
from stariter import StarIter

###


class TestStarIter(unittest.TestCase):

    def test_num_0(self):
        siter = StarIter()
        print siter
        for i in siter:
            print "shouldnt print", i
            self.assertTrue(False)
        self.assertTrue(True)

    def test_num_1(self):
        siter = StarIter().addRange("a", 3)
        print siter
        cnt = 0
        for i in siter:
            cnt += 1
            print i.a
        self.assertTrue(cnt == 3)

    def test_num_2(self):
        siter = StarIter().addRange("a", 3, 6)
        print siter
        cnt = 0
        for i in siter:
            print i.a
            cnt += 1
        self.assertTrue(cnt == 3)

    def test_num_22(self):
        cnt = 0
        for i in StarIter().addRange("a", 3).addRange("b", 3, 6):
            print (i.a, i.b)
            cnt += 1
        self.assertTrue(cnt == 9)

    def test_list_0(self):
        siter = StarIter()
        siter.addList("l0", [])
        print siter
        for i in siter:
            self.assertTrue(False)
        self.assertTrue(True)

    def test_list_1(self):
        siter = StarIter()
        siter.addList("l0", ["a", "b"])
        print siter
        cnt = 0
        for i in siter:
            cnt += 1
            print i.l0
        self.assertTrue(cnt == 2)

    def test_list_3(self):
        siter = StarIter()
        siter.addList("l0", ["a", "b", "c", "d"])
        siter.addList("l1", ["1", "2", "3", "4"])
        print siter
        cnt = 0
        for i in siter:
            print (i.l0, i.l1),
            cnt += 1
        print
        self.assertTrue(cnt == 16)

    def test_glob_1(self):
        siter = StarIter()
        siter.addGlob("path", "lib/stariter/*.py")
        print siter
        for i in siter:
            print i.path

    def test_glob_2(self):
        siter = StarIter()
        siter.addGlob("path_a", "lib/stariter/*.py")
        siter.addGlob("path_b", "lib/stariter/*.py")
        print siter
        for i in siter:
            print "a=%s b=%s" % (i.path_a, i.path_b)
