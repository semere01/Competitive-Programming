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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.levelOrder(root)
        ans = []
        for d in self.data:
            if len(d):
                ans.append(d[-1])
        # if (root == None):
        #     return []
        # ans = []
        # node = root
        # while (node):
        #     ans.append(node.val)
        #     if (node.right):
        #         node = node.right
        #     elif (node.left):
        #         node = node.left
        #     else:
        #         break
        
        return ans
