class Solution:
    def maxDepth(self, root) -> int:
        return self.dd(root, 0)

    def dd(self, root, depth:int):
        if (root == None):
            return depth
        return max(self.dd(root.left, depth+1), self.dd(root.right, depth+1))


