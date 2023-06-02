from collections import defaultdict, deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.cache = {}
        self.visited = set()
    def optimalJuice(self, node:TreeNode):
        if node in self.cache:
            print(f'{node.val} = {node.val}')
            return self.cache[node]
        if not node.left and not node.right:
            return node.val
        myValue = node.val
        leftVal = 0
        if (node.left):
            leftVal = self.optimalJuice(node.left)
        rightVal = 0
        if (node.right):
            rightVal = self.optimalJuice(node.right)

        leftleft = 0
        if (node.left and node.left.left):
            leftleft = self.optimalJuice(node.left.left)

        leftright = 0
        if (node.left and node.left.right):
            leftright = self.optimalJuice(node.left.right)

        rightleft = 0
        if (node.right and node.right.left):
            rightleft = self.optimalJuice(node.right.left)
        rightright = 0
        if (node.right and node.right.right):
            rightright = self.optimalJuice(node.right.right)
        v = max( leftVal+rightVal,  myValue+leftleft+leftright+rightleft+rightright) 
        self.cache[node] = v
        return v

    def rob(self, root: Optional[TreeNode]) -> int:
        return self.optimalJuice(root)
        

        
        
            
