__author__ = 'liuxiyun'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if root == None:
            return None
        min_node = root.val
        min_diff = sys.maxint
        node = root
        while node != None:
            if target == node:
                return target
            else:
                if min_diff > abs(target-node.val):
                    min_diff = abs(target-node.val)
                    min_node = node.val
                if target < node.val:
                    node = node.left
                else:
                    node = node.right
        return min_node
                    