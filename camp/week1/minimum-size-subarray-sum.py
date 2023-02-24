class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        nums.sort()

        total = 0
        count = 0
        for i in range(len(nums) - 1, -1, -1):
            if (total) > target:
                break
            total += nums[i]
            count += 1
        return count