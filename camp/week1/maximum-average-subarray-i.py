class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        biggest = 0

        for i in range(k):
            biggest += nums[i]
        curr = biggest
        
        for i in range(k, len(nums)):
            # curr = biggest + nums[k+1] - nums[i-k]
            curr = curr + nums[i] - nums[i-k]
            if (curr > biggest):
                biggest = curr
        
        return biggest/k
print(Solution().findMaxAverage([1,12,-5,-6,50,3], 4))