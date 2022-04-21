class Solution:
    def perm(self, x): 
        ans = 0
        for i in range(1, x):
            ans = ans + i
        return ans
    def numIdenticalPairs(self, nums: list[int]) -> int:
        counts = {}
        totalGoodPairs = 0
        for x in nums:
            if (x not in counts.keys()):
                counts[x] = nums.count(x)

        for count in counts.keys():
            currentGoodPairs = 0
            if counts[count] > 1:
                currentGoodPairs += self.perm(counts[count])
            totalGoodPairs += currentGoodPairs
        return totalGoodPairs;
            

        
# [1,2,3,1,1,3]
# output 2
# expected 4
print("final answer: ", Solution().numIdenticalPairs([1,2,3,1,1,3]))
