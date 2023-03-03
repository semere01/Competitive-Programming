class Solution():
    def maxOperations(self, nums, k):
        maxOps = 0
        counter = collections.Counter()
        for i in nums:
            if (k-i in counter) and counter[k-i]:
                counter[k-i] -= 1
                maxOps += 1
            else:
                counter[i] += 1
        return maxOps