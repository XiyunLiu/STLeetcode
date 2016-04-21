__author__ = 'liuxiyun'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return []
        mid,new_root = self.do(root)
        return new_root
    def do(self,node):
        if node.left:
            mid,root = self.do(node.left)
            if node.right:
                mid.left = TreeNode(node.right.val)
            mid.right = TreeNode(node.val)
            return mid.right,root
        else:
            return node,node

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None or (root.left == None and root.right == None):
            return root
        new_root = self.upsideDownBinaryTree(root.left)
        mid = root.left
        mid.left = root.right
        mid.right = root
        root.left = None
        root.right = None
        return new_root

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        preorder = []
        stack = []
        if root:
            stack.append(root)
        else:
            return []
        while stack:
            node= stack.pop()
            preorder.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            elif node.left:
                stack.append(TreeNode(-1))
        new_root = node = TreeNode(preorder.pop())
        while preorder:
            newnode = TreeNode(preorder.pop())
            if newnode.val==-1:
                node.left = None
            else:
                node.left = newnode
            if preorder:
                node.right = TreeNode(preorder.pop())
                node = node.right
        return new_root
# [2,1]

# [2,1]
