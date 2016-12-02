#!/usr/bin/env python
#
# ~/projects/python/miter/miter-test ---
#
# $Id: StarIter.py,v 1.7 2011/01/31 20:31:21 harley Exp $
#

import glob
import random

class StarIter(object):
  def __init__(self):
    # the name is the key.
    self.ranges=dict()
  #
  def __iter__(self):
    # make a copy of this object and ranges and give it to the iterator,
    # as iterator modifies the internal state.
    return StarIterIter(self)
  # Make a duplicate of ourselves and the Ranges contained.
  def copy(self):
    dup=StarIter()
    for r in self.ranges.itervalues():
      r_dup=r.copy()
      dup.ranges[r_dup.name]=r_dup
    return dup
  #
  def __str__(self):
    s=["StarIter<"]
    if len(self.ranges)>0:
      for r in self.ranges.itervalues():
        s.append("{0!s}".format(r))
        s.append("; ")
      s.pop()
    s.append(">")
    return "".join(s)

  #
  def pushRangeObj(self,range):
    self.ranges[range.name]=range
    return self
  #
  def addRange(self,name,start,end):
    return self.pushRangeObj(StarRangeNum(name,start,end))
  def addList(self,name,list):
    return self.pushRangeObj(StarRangeList(name,list))
  def addGlob(self,name,glob):
    return self.pushRangeObj(StarRangeGlob(name,glob))
  #
  def randomOrder(self):
    return StarIterIter(self,randomOrder=True)
  #
  def shuffledOrder(self):
    lst=[]
    for i in StarIterIter(self):
      lst.append(i.copy())
    random.shuffle(lst)
    return lst

##########

class StarIterIter(object):
  def __init__(self,parent,randomOrder=False):
    # make a copy as we modifiy its internal state.
    self.parent=parent.copy()
    self.iterdict=dict()
    self.r_idx=-1
    self.r_lst=parent.ranges.values()
    self.randomOrder=randomOrder

  def __iter__(self):
    return self

  def next(self):
    if self.r_idx==-1:
      if len(self.r_lst)==0:
        #print "StarIterIter:next(): len(self.r_lst)==0"
        raise StopIteration
      for r in self.r_lst:
        try:
          self.iterdict[r.name]=r.i_reset(self.randomOrder)
        except StopIteration:
          raise StopIteration
      self.r_idx=0
      return self.iterdict
    #
    for r in self.r_lst:
      try:
        self.iterdict[r.name]=r.i_next()
        return self.iterdict
      except StopIteration:
        self.iterdict[r.name]=r.i_reset(self.randomOrder)
    raise StopIteration

##########

class StarRangeNum(object):
  def __init__(self,name,start,end):
    self.name=name
    self.start=start
    self.end=end
    self.i=None
  #
  def copy(self):
    return StarRangeNum(self.name,self.start,self.end)
  def __str__(self):
    return "StarRangeNum<{0!s}:{1!s}..{2!s}>".format(self.name,self.start,self.end)
  #
  def i_reset(self,randomOrder=False):
    self.i=self.start
    return self.i
  def i_next(self):
    self.i=self.i+1
    if self.i>=self.end:
      raise StopIteration
    return self.i

class StarRangeList(object):
  def __init__(self,name,lst):
    self.name=name
    self.lst=lst[:]
    self.i=None
  #
  def copy(self):
    return StarRangeList(self.name,self.lst)
  def __str__(self):
    return "StarRangeList<{0!s}:{1!s}>".format(self.name,self.lst)
  #
  def i_reset(self,randomOrder=False):
    if randomOrder:
      random.shuffle(self.lst)
    #print "StarRangeList:i_reset: ",self.name
    self.i=0
    if len(self.lst)==0:
      raise StopIteration
    return self.lst[self.i]
  def i_next(self):
    self.i=self.i+1
    if self.i>=len(self.lst):
      raise StopIteration
    return self.lst[self.i]

class StarRangeGlob(object):
  def __init__(self,name,glob):
    self.name=name
    self.glob=glob
    self.lst=None
    self.i=None
  #
  def copy(self):
    return StarRangeGlob(self.name,self.glob)
  def __str__(self):
    return "StarRangeGlob<{0!s}:{1!s}>".format(self.name,self.glob)
  #
  def i_reset(self,randomOrder=False):
    # reexpand the glob each time iteration starts.
    self.lst=glob.glob(self.glob)
    #
    if randomOrder:
      random.shuffle(self.lst)
    #print "StarRangeList:i_reset: ",self.name
    self.i=0
    if len(self.lst)==0:
      raise StopIteration
    return self.lst[self.i]
  def i_next(self):
    self.i=self.i+1
    if self.i>=len(self.lst):
      raise StopIteration
    return self.lst[self.i]

# Local Variables:
# mode: python
# End:
