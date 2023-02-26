class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        window_sum = 0
        min_len = float('inf')
        while right < len(nums):
            window_sum += nums[right]
            right += 1
            while window_sum >= target:
                min_len = min(min_len, right - left)
                window_sum -= nums[left]
                left += 1
        if min_len == float('inf'):
            return 0
        return min_len
