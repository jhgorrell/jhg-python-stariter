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
        print "test_num_1 =========="
        cnt = 0
        for i in StarIter().addRange("a", 3).addRange("b", 3, 6):
            print (i.a, i.b)
            cnt += 1
        self.assertTrue(cnt == 9)

#     def test_num_2(self):
#         print "test_num_2 =========="
#         siter = StarIter()
#         siter.addRange("a", 0, 3)
#         siter.addRange("b", 10, 12)
#         print siter
#         for i in siter:
#             print i["a"], i["b"]
#
#     def test_list_0(self):
#         print "test_list_0 =========="
#         siter = StarIter()
#         siter.addList("l0", [])
#         print siter
#         for i in siter:
#             print i["l0"]
#
#     def test_list_1(self):
#         print "test_list_1 =========="
#         siter = StarIter()
#         siter.addList("l0", ["a", "b"])
#         print siter
#         for i in siter:
#             print i["l0"]
#
#     def test_list_2(self):
#         print "test_list_1 =========="
#         siter = StarIter()
#         siter.addList("l0", ["a", "b"])
#         siter.addList("l1", [])
#         print siter
#         for i in siter:
#             print "shouldnt print", i
#             raise SystemError
#
#     def test_list_3(self):
#         print "test_list_3 =========="
#         iter = StarIter()
#         siter.addList("l0", [1, 2, 3, 4, 5, 6])
#         print siter
#         for i in siter.randomOrder():
#             print i["l0"]
#
#     def test_list_3(self):
#         print "test_list_3 =========="
#         siter = StarIter()
#         siter.addList("l0", ["a", "b", "c", "d"])
#         siter.addList("l1", ["1", "2", "3", "4"])
#         print siter
#         for i in siter.randomOrder():
#             print i["l0"] + i["l1"],
#         print
#
#     def test_list_4(self):
#         print "test_list_4 =========="
#         siter = StarIter()
#         siter.addList("l0", ["a", "b", "c", "d"])
#         siter.addList("l1", ["1", "2", "3", "4"])
#         print siter
#         for i in siter.shuffledOrder():
#             print i["l0"] + i["l1"],
#         print
#
#     def test_glob_1(self):
#         print "test_glob_1 =========="
#         siter = StarIter()
#         siter.addGlob("file", "*")
#         print siter
#         for i in siter:
#             print i["file"]
#
#     def test_glob_2(self):
#         print "test_glob_1 =========="
#         siter = StarIter()
#         siter.addGlob("file-a", "Star*.py")
#         siter.addGlob("file-b", "Star*.py")
#         print siter
#         for i in siter:
#             print "file-a=", i["file-a"], "file-b", i["file-b"]
