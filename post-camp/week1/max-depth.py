# # Definition for a Node.
# class Node:
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children

class Solution:
    def maxDepth(self, root) -> int:
        if not root: return 0
        def maxD(node, curr_height):
            if (len(node.children) == 0):
                return curr_height
            return ((max([maxD(child, curr_height+1) for child in node.children])))
        return maxD(root, 1)
