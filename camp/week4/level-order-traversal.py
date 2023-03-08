# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root) :
        self.data = []
        self.traverse(root, 0)
    
    def traverse(self, root, level):
        if (root == None):
            return
        while (len(self.data) < level +1):
            self.data.append([])
        self.data[level].append(root.val)
        if (root.left):
            self.traverse(root.left, level +1)
        if (root.right):
            self.traverse(root.right, level +1)