class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = ''
        max_len = 0
        
        for char in s:
            while char in substr:
                substr = substr[1:]
            substr += char
            max_len = max(max_len, len(substr))
        
        return max_len
