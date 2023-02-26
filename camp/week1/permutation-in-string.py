class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = {}
        freq2 = {}
        for char in s1:
            freq1[char] = freq1.get(char, 0) + 1
        left = 0
        right = 0
        while right < len(s2):
            freq2[s2[right]] = freq2.get(s2[right], 0) + 1
            right += 1
            if right - left > len(s1):
                freq2[s2[left]] -= 1
                if freq2[s2[left]] == 0:
                    del freq2[s2[left]]
                left += 1
            if freq1 == freq2:
                return True
        return False
