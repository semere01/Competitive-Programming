class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        max_len = 0
        counts = {}
        while right < len(s):
            counts[s[right]] = counts.get(s[right], 0) + 1
            right += 1
            while right - left - max(counts.values()) > k:
                counts[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left)
        return max_len