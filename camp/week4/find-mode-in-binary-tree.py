# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root):
        count_map = {}
        largestKeys = []
        self.largestCount = -1
        self.dd(root, count_map, largestKeys)
        return largestKeys
    
    def dd(self, root, countMap, largestKeys):
        if root == None:
            return
        countMap[root.val] = countMap.get(root.val, 0) + 1
        if self.largestCount == countMap[root.val]:
            largestKeys.append(root.val)
        elif self.largestCount < countMap[root.val]:
            while(largestKeys):
                largestKeys.pop()
            largestKeys.append(root.val)
            self.largestCount = countMap[root.val]
        self.dd(root.left, countMap,  largestKeys)
        self.dd(root.right, countMap,  largestKeys)