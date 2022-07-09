

class Solution:
    def topKFrequent(self, nums, maxFreq):
        map = {}
        invMap = [ [] ] * len(nums) 
        listToReturn = []

        for n in nums:
            if n not in map:
                map[n] = 0
            map[n] += 1
        for k,v in map.items():
            invMap[v-1] = invMap[v-1] + [k]
        # print(invMap)
        while len(listToReturn) < maxFreq:
            for i in range(len(invMap)-1, -1, -1):
                invMap[i] = sorted(invMap[i])
                for v in invMap[i]:
                    listToReturn = listToReturn + [v]
                    if len(listToReturn) == maxFreq:
                        return listToReturn
        
words = ["i","love","leetcode","i","love","coding"]
k = 1
print(Solution().topKFrequent(words, k))
