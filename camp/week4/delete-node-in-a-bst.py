# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root, key: int):
        node = self.searchBST(root)
        if (node == None): return root
        if (root.val == key): return None

        parent = node[0]
        child = parent.right if node[1] else parent.left
        
        if (child.left == None and child.right == None):
            if (node[1]):
                parent.right = None
            else:
                parent.left = None
            return root
        if (child.left == None or child.right == None):
            nextChild = child.left if child.left != None else child.right
            if (node[1]):
                parent.right = nextChild
            else:
                parent.left = nextChild
            return root
        
        inf_list = self.infix(root)
        min_node = inf_list[0]
        if (min_node.right != None):
            inf_list[-2].left = min_node.right
        if (node[1]):
            parent.right = min_node
            min_node.left = child.left
            min_node.right = child.right
        else:
            parent.left = min_node
            min_node.left = child.left
            min_node.right = child.right
        return root
    
    def infix(self, root):
        if (root == None):
            return
        data = []
        if root.left != None:
            data = data + self.infix(root.left)
        data.append(root)
        if (root.right != None):
            data = data + self.infix(root.right)
        
        return data
        







    

             

    def searchBST(self, root, val: int):
        if (root == None or (root.right == None and root.left == None)):
            return None
        if (root.right != None and root.right.val == val):
            return [root, 1]
        if (root.left != None and root.left.val == val):
            return [root, 0]

        if (val > root.val):
            return self.searchBST(root.right, val)
        if (val < root.val):
            return self.searchBST(root.left, val)
