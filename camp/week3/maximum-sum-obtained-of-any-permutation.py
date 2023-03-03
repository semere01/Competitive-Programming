from typing import List
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        count = [0] * n
        for l, r in requests:
            count[l] += 1
            if r+1 < n:
                count[r+1] -= 1
        for i in range(1, n):
            count[i] += count[i-1]
        count.sort()
        nums.sort()
        res = 0
        for i in range(n):
            res += count[i] * nums[i]
        return res % 10**9 + 7