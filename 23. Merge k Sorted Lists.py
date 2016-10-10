__author__ = 'liuxiyun'
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = fakeHead = ListNode(0)
        withVal = [(x.val,x) for x in lists if x != None]
        heapq.heapify(withVal)
        while withVal:
            minVal = heapq.heappop(withVal)
            fakeHead.next = ListNode(minVal[0])
            fakeHead = fakeHead.next
            if minVal[1].next:
                heapq.heappush(withVal,(minVal[1].next.val,minVal[1].next))
        return head.next


