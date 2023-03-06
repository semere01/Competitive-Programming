class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        my_dict = defaultdict(int)
        sum_, res = 0, 0
        my_dict[0] = 1
        for n in nums:
            sum_ += n
            res += my_dict.get(sum_ - goal, 0)
            my_dict[sum_]+=1
        return res