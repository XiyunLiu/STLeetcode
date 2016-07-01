__author__ = 'liuxiyun'

# O(log n)
# find the smallest one larger than p
# It just like the binary search in a sorted list.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        suc = None
        node = root
        while node:
            if p.val<node.val:
                suc = node
                node = node.left
            else:
                node = node.right
        return suc


