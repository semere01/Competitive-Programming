class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if (len(nums) <= 4):
            return 0
        nums.sort()
        possibilities = []
        for i in range(4):
            possibilities.append(nums[i-4] - nums[i])
        return min(possibilities)

