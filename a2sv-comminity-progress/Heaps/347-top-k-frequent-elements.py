# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

class Solution:
    def topKFrequent(self, nums: list[int], maxFreq: int) -> list[int]:
        map = {}
        invMap = [ [] ] * len(nums) 
        print(invMap)
        listToReturn = []

        for n in nums:
            if n not in map:
                map[n] = 0
            map[n] += 1
        for k,v in map.items():
            invMap[v-1] = invMap[v-1] + [k]
        while len(listToReturn) < maxFreq:
            for i in range(len(invMap)-1, -1, -1):
                listToReturn += invMap[i]
                if len(listToReturn) == maxFreq:
                    return listToReturn
nums = [5, 1, -1, -8, -7, 8, -5, 0, 1, 10, 8, 0, -4, 3, -1, -1, 4, -5, 4, -3, 0, 2, 2, 2, 4, -2, -4, 8, -7, -7, 2, -8, 0, -8, 10, 8, -8, -2, -9, 4, -7, 6, 6, -1, 4, 2, 8, -3, 5, -9, -3, 6, -8, -5, 5, 10, 2, -5, -1, -5, 1, -3, 7, 0, 8, -2, -3, -1, -5, 4, 7, -9, 0, 2, 10, 4, 4, -4, -1, -1, 6, -8, -9, -1, 9, -9, 3, 5, 1, 6, -1, -2, 4, 2, 4, -6, 4, 4, 5, -5]
k = 7
print(Solution().topKFrequent(nums, k))
