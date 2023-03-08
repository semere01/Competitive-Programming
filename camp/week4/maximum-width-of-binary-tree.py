# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def widthOfBinaryTree(self, root) -> int:
        data = []
        self.dd(root, 0, 0, data)
        maxWidth = 0
        for d in data:
            if d[1]-d[0] > maxWidth:
                maxWidth = d[1]-d[0]
        return maxWidth+1
    
    def dd(self, root, level, x, data):
        if (root == None):
            return
        
        while(len(data) < level+1):
            data.append([])
        
        if data[level] == []:
            data[level] = [x,x]
        elif x < data[level][0]:
            data[level][0] = x
        elif x > data[level][1]:
            data[level][1] = x
       
        
        self.dd(root.left, level+1, 2*x, data)
        self.dd(root.right, level+1, (2*x)+1, data)
        
        
        
        
        
