class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)-1):
            if (nums[i] == nums[i+1]):
                nums[i] = nums[i]*2
                nums[i+1] = 0

        a = []
        for n in nums:
            if (n != 0):
                a.append(n)

        while len(a) < len(nums):
            a.append(0)
        return a
