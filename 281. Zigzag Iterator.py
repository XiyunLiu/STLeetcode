__author__ = 'liuxiyun'
class ListNode(object):
    def __init__(self,val):
        self.val = val
        self.next = None

class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        v1Pre = ListNode(0)
        pre1 = v1Pre
        for node in v1:
            pre1.next = ListNode(node)
            pre1 = pre1.next
        v2Pre = ListNode(0)
        pre2 = v2Pre
        for node in v2:
            pre2.next = ListNode(node)
            pre2 = pre2.next
        self.v1 = v1Pre.next
        self.v2 = v2Pre.next
        self.cur = self.v1

    def next(self):
        """
        :rtype: int
        """
        if self.v1 == None:
            tmp = self.v2.val
            self.v2 = self.v2.next
            return tmp
        if self.v2 == None:
            tmp = self.v1.val
            self.v1 = self.v1.next
            return tmp
        if self.cur == self.v1:
            tmp = self.v1.val
            self.v1 = self.v1.next
            self.cur = self.v2
            return tmp
        if self.cur == self.v2:
            tmp = self.v2.val
            self.v2 = self.v2.next
            self.cur = self.v1
            return tmp

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.v1 == None and self.v2 == None:
            return False
        return True

v1 = [1,2]
v2 = [3,4,5,6]
# Your ZigzagIterator object will be instantiated and called as such:
i, v = ZigzagIterator(v1, v2), []
while i.hasNext():
    v.append(i.next())
print v