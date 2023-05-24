class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = int(len(costs)/2)
        cheapDiff =sorted(costs, key=lambda x: x[0]-x[1])
        ans = sum([i[0] for i in cheapDiff[:n]]) + sum(i[1] for i in cheapDiff[n:])
        return ans