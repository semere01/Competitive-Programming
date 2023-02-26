class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)                
        # cnt = 0
        # for i in range(n):
        #     curr_sum = 0
        #     for j in range(i, n):
        #         curr_sum += nums[j]
        #         if curr_sum == k:
        #             cnt += 1
        # return cnt
        d ={0:1}
        curr_sum = 0 
        cnt = 0
        for i in range(n):
            curr_sum += nums[i]
            if curr_sum-k in d:
                cnt += d[curr_sum-k]
            d.setdefault(curr_sum, 0)
            d[curr_sum] += 1
        return cnt



