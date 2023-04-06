class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        total = edges[0]+edges[1]
        for i in total:
            if total.count(i) == 2:
                return i