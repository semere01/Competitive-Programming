class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        sortedNums = sorted(nums)
        biggestSum = sortedNums[0]
        l = 0
        r = len(sortedNums) - 1
        while l < r:
            currentSum = sortedNums[l] + sortedNums[r]
            if biggestSum < currentSum: biggestSum = currentSum
            l+=1
            r-=1
        return(biggestSum)


