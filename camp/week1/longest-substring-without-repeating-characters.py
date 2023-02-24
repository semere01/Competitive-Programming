class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (len(s) < 2):
            return (len(s))
        s = list(s)

        l = 0
        r = 0
        largest = 0
        memSet = set()
        while (r < len(s)):
            if (s[r] not in memSet):
                memSet.add(s[r])
            else:
                if ( largest < len(memSet)):
                    largest = len(memSet)
                memSet.remove(s[r])
                while (s[l] != s[r]):
                    if (s[l] in memSet): memSet.remove(s[l])
                    l += 1
                l += 1
                memSet.add(s[l])
            r += 1
        
        return largest

print(Solution().lengthOfLongestSubstring("pwwkew"))
