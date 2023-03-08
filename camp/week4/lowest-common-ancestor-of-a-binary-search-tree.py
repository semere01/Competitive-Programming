# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.check(root, p, q)

    
    def check(self, root, q, p):
        if (root == None):
            return None

        l = self.check(root.left, q, p)
        r = self.check(root.right, q, p)
        s = None

        if root.val == q.val:
            s = q
        if root.val == p.val:
            s = p
        
        if l and r:
            return root
        if s and r:
            return s
        if s and l:
            return s
        if l:
            return l
        if r:
            return r
        if s:
            return s
        return None


        



