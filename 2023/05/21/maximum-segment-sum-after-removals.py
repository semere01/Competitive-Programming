from typing import List


class Union:
    def __init__(self, data):
        size = len(data)
        # self.data = data
        self.reps = [i for i in range(len(data))]
        self.activated = [0] * size
        self.sum = [d for d in data]
        self.size = [1] * size
        self.maxSum = 0
    
    def rep(self, x: int) -> int:
        stack = [self.reps[x]]
        while (stack):
            current = stack[-1]
            if current == self.reps[current]:
                for element in stack:
                    self.reps[element] = current
                return current
            else:
                stack.append(self.reps[current])
    
    def activate(self, i:int):
        self.activated[i] = 1
        self.maxSum = max(self.sum[i], self.maxSum)
        if (i > 0 and self.activated[i-1]):
            self.join(i, i-1)
        if (i < (len(self.reps) -1) and self.activated[i+1]):
            self.join(i, i+1)

    def join(self, x:int, y: int) -> int:
        x_rep = self.rep(x)
        y_rep = self.rep(y)
        if (x_rep != y_rep):
            if (self.size[y_rep] > self.size[x_rep]):
                self.reps[x_rep] = y_rep
                self.size[y_rep] += self.size[x_rep]
                self.sum[y_rep] += self.sum[x_rep]
                self.maxSum = max(self.sum[y_rep], self.maxSum)
            else:
                self.reps[y_rep] = x_rep
                self.size[x_rep] += self.size[y_rep]
                self.sum[x_rep] += self.sum[y_rep]
                self.maxSum = max(self.sum[x_rep], self.maxSum)

class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        union = Union(nums)
        ans = []
        for i in range(len(removeQueries)-1, -1, -1):
            ans.append(union.maxSum)
            query = removeQueries[i]
            union.activate(query)
        return ans[::-1]

print(Solution().maximumSegmentSum([1,2,5,6,1], [0,3,2,4,1]))
