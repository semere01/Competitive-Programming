class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        counts = {}
        nums_as_set = set(nums)
        totalCount = 0
        for num in nums_as_set:
            counts[num] = 0

        for num in nums:
            counts[num] += 1
        for num in nums_as_set:
            totalCount += self.permutate(counts[num])

        return int(totalCount)

    def permutate(self, num: int) -> int:
        if (num <= 1):
            return 0
        return (num * (num-1)) / 2
