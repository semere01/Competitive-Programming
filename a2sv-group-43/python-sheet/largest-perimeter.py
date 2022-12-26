class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort()

        for i in range(len(nums) - 1, 1, -1):
            if nums[i] < nums[i - 2] + nums[i - 1]:
                return nums[i - 2] + nums[i - 1] + nums[i]

        return 0
