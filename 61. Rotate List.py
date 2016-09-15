__author__ = 'liuxiyun'
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0:
            return head
        pointer_1, pointer_2 = head, head
        j = k
        while j > 1 and pointer_2.next:
            pointer_2 = pointer_2.next
            j -= 1
        # k > length
        if j != 1:
            j = k % (k-j+1)
            if j == 0:
                return head
            pointer_2 = head
            while j > 1 and pointer_2:
                pointer_2 = pointer_2.next
                j -= 1
        pre_node = None
        while pointer_2 and pointer_2.next: # []
            pre_node = pointer_1
            pointer_1 = pointer_1.next
            pointer_2 = pointer_2.next
        if pre_node: # if move
            pointer_2.next = head
            pre_node.next = None
        return pointer_1


    # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        end = dummy
        new_head_pre = dummy
        length = 0
        # Get the length
        while end.next:
            end = end.next
            length += 1
        print length
        j = length-k%length # how many step should new_head_pre move
        print j
        while j>0:
            new_head_pre = new_head_pre.next
            j -= 1
        end.next = head
        dummy.next = new_head_pre.next
        new_head_pre.next = None
        return dummy.next

