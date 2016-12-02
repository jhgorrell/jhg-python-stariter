#
# jhg-python-stariter/lib/stariter/stariter.py ---
#

import pdb
import glob
import random

#####


class StarIter(object):

    def __init__(self):
        self._range_lst = []
        self._range_by_name = dict()

    def __str__(self):
        s = ["StarIter<"]
        if len(self._range_lst) > 0:
            for r in self._range_lst:
                s.append("{0!s}".format(r))
                s.append("; ")
            s.pop()
        s.append(">")
        return "".join(s)

    def __iter__(self):
        # make a copy of this object and ranges and give it to the iterator,
        # as iterator modifies the internal state.
        return StarIterIter(self)
    # Make a duplicate of ourselves and the Ranges contained.

    def copy(self):
        dup = StarIter()
        for r in self._range_lst:
            dup.appendRangeObj(r.copy())
        return dup

    def appendRangeObj(self, range_obj):
        self._range_lst.append(range_obj)
        self._range_by_name[range_obj.name] = range_obj
        return self

    def addRange(self, name, *args, **kwargs):
        # pdb.set_trace()
        if len(args) == 1 and type(args[0]) == int:
            return self.appendRangeObj(StarRangeNum(name, 0, args[0]))
        if len(args) == 2 and type(args[0]) == int and type(args[1]) == int:
            return self.appendRangeObj(StarRangeNum(name, args[0], args[1]))
        #
        if len(args) == 1 and type(args[0]) == list:
            return self.appendRangeObj(StarRangeList(name, args[0]))
        #
        raise ValueError("")

    def addList(self, name, lst):
        return self.appendRangeObj(StarRangeList(name, lst))

    def addGlob(self, name, glob_pat):
        return self.appendRangeObj(StarRangeGlob(name, glob_pat))


##########


class StarIterIter(object):

    def __init__(self, parent):
        # make a copy as we modifiy its internal state.
        self._parent = parent.copy()
        self._state = None

    def __iter__(self):
        return self

    def setValue(self, name, value):
        setattr(self, name, value)

    def i_reset(self):
        self._state = "ok"
        for r in self._parent._range_lst:
            try:
                r.i_reset()
            except StopIteration:
                raise StopIteration
            self.setValue(r.name, r.value)
        return self

    def next(self):
        if not self._parent._range_lst:
            raise StopIteration("Nothing to iterate on.")
        #
        if self._state is None:
            return self.i_reset()
        #
        for r in self._parent._range_lst:
            try:
                r.i_next()
                self.setValue(r.name, r.value)
                return self
            except StopIteration:
                r.i_reset()
                self.setValue(r.name, r.value)
        #
        raise StopIteration

##########


class StarRangeBase(object):

    def __init__(self, name):
        self._name = name
        self._value = None

    def __iter__(self):
        self.i_reset()
        return self

    def next(self):
        return self.i_next()

    def i_reset(self):
        self._idx = None
        self._value = None
        return self

    def i_next(self):
        raise StopIteration("%s" % (self.__class__.__name__))

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value

    def __str__(self):
        return "<%s %r>" % (self.__class__.__name__, self._name)


class StarRangeNum(StarRangeBase):

    def __init__(self, name, start, end):
        super(StarRangeNum, self).__init__(name=name)
        self._idx_start = start
        self._idx_end = end

    def copy(self):
        return StarRangeNum(self._name, self._idx_start, self._idx_end)

    def __str__(self):
        return "StarRangeNum<{0!s}:{1!s}..{2!s}>".format(self._name, self._idx_start, self._idx_end)

    def i_reset(self):
        self._idx = self._idx_start
        self._value = self._idx

    def i_next(self):
        if self._idx is None:
            self._idx = self._idx_start
        else:
            self._idx += 1
        #
        if self._idx >= self._idx_end:
            raise StopIteration
        self._value = self._idx


class StarRangeList(StarRangeBase):

    def __init__(self, name, lst):
        super(StarRangeList, self).__init__(name=name)
        self._lst = lst[:]
        self._idx = None

    def copy(self):
        return StarRangeList(self._name, self._lst)

    def __str__(self):
        return "StarRangeList<{0!s}:{1!s}>".format(self._name, self._lst)

    def i_reset(self):
        self._idx = 0
        if len(self._lst) == 0:
            raise StopIteration
        self._value = self._lst[self._idx]

    def i_next(self):
        self._idx = self._idx + 1
        if self._idx >= len(self._lst):
            raise StopIteration
        self._value = self._lst[self._idx]


class StarRangeGlob(StarRangeList):

    def __init__(self, name, glob_pat):
        super(StarRangeList, self).__init__(name=name)
        self._glob_pat = glob_pat
        self._lst = None
        self._idx = None

    def copy(self):
        return StarRangeGlob(self._name, self._glob_pat)

    def __str__(self):
        return "StarRangeGlob<{0!s}:{1!s}>".format(self._name, self._glob_pat)

    def i_reset(self):
        self._idx = 0
        self._lst = glob.glob(self._glob_pat)
        if len(self._lst) == 0:
            raise StopIteration()
        self._value = self._lst[self._idx]
