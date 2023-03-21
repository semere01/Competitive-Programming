# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root , val: int) :
        pass
    def dd(self, root, val):
        if (root == None):
            return TreeNode(val)
        if val < root.val:
            return self.dd(root.left)
        if val > root.val:
            return self.dd(root.right)
        