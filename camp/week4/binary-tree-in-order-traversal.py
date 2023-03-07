# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.lpr(root)
    


    def lpr(self, node: TreeNode) -> list[int]:
        if (node == None):
            return []
        ans = []
        if (node.left != None):
            ans += self.lpr(node.left)
        ans.append(node.val)
        if (node.right != None):
            ans += self.lpr(node.right)
        return ans
