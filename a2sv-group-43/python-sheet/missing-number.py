
class Solution:
    def missingNumber(self, nums) -> int:
        data = [True for i in range(len(nums)+1)]
        for num in nums:
            data[num] = False

        for i in range(len(data)):
            current = data[i]
            if current:
                return i
