class Solution:
    def isSymmetric(self, root) -> bool:
        data = []
        self.infix(root, data, 0, 0)
        center = len(data) // 2
        return data[:center] == data[center+1:][::-1]
    
    def infix(self,root, data, row, col):
        if (root == None):
            return
        self.infix(root.left, data, row+1, abs(col+1))
        data.append((root.val, row, col))
        self.infix(root.right, data, row+1, abs(col+1))


