__author__ = 'liuxiyun'
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxLength = 0
        if root == None:
            return 0
        return self.helper(root,1)

    def helper(self, node, length):
        if node.left and node.val - node.left.val == -1:
            left = length + 1
        else:
            left = 1
        if node.right and node.val - node.right.val == -1:
            right = length + 1
        else:
            right = 1
        self.maxLength = max(self.maxLength, left, right)
        if node.left:
            self.helper(node.left, left)
        if node.right:
            self.helper(node.right, right)
        return self.maxLength