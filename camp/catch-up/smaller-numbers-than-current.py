class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        finalList = []
        for i in nums:
            currentCount = 0
            for j in nums:
                if  j < i:
                    currentCount += 1
            finalList.append(currentCount)
        return finalList