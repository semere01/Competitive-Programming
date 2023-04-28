# Definition for a binary tree node.
# from collections import defaultdict


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root):
        queue = [root]
        sums = []
        while queue:                    
            cutOff= len(queue)
            curr_sum = 0
            for i in range(cutOff):
                node = queue[i]
                if (node):
                    curr_sum += node.val
            sums.append(curr_sum/cutOff)
            for i in range(cutOff):
                node = queue[i]
                if (node):
                    if (node.left):
                        queue.append(node.left)
                    if (node.right):
                        queue.append(node.right)
            for i in range(cutOff):
                queue.pop(0)
        return sums




