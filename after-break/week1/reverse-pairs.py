class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        arr = []
        res = 0
        nums = nums[::-1]

        for x in nums:
            res += bisect.bisect_left(arr,(x+1)//2)
            insort(arr,x)
        return res
        