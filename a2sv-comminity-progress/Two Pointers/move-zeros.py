class Solution:
    # def moveZeroes(self, nums: List[int]) -> None:
    def moveZeroes(self, nums):
        if nums:
            # if nums.count(0) == len(nums): return
            i = 0
            length = len(nums)
            while i < length:
                if nums[i] == 0:
                    nums.remove(0)
                    nums.append(0)
                    lenght -= 1
                else:
                    i += 1




        