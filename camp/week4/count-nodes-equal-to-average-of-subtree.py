# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root) -> int:
        return self.dd(root)[2]
        # def dd();
    
    # [node_count, total, gold_count]
    def dd(self, root):
        if (root) == None:
            return [0,0,0]
        if (root.left == None and root.right == None):
            return [1, root.val, 1]
        [node_count, total, gold_count] = self.dd(root.left)
        right_list = self.dd(root.right)
        

        node_count += right_list[0]
        total += right_list[1]
        gold_count += right_list[2]

        node_count += 1
        total += root.val
        if (total // node_count) == root.val:
            gold_count +=1 
        return [node_count, total, gold_count]
        
            
            
            
    