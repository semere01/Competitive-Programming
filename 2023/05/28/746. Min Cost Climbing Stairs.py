class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        return min(self.costAtIndex(cost, {}, 0),self.costAtIndex(cost, {}, 1))
        pass
    
    def costAtIndex(self, cost: List[int], cache, index: int):
        if (index in cache.keys()):
            return cache[index]
        if (index >= len(cost)):
            return 0
        if (index >= len(cost) - 2):
            return cost[index]
        cache[index] = cost[index] + min(self.costAtIndex(cost, cache, index+1),self.costAtIndex(cost, cache, index+2))
        return cache[index]

