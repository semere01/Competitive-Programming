class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        indices = []
        s = list(s)
        if (len(p) != len(set(p))):
            for i in range(len(s)-len(p)+1):
                if sorted(s[i:i+len(p)]) == sorted(p):
                    indices.append(i)
        else: 
            for i in range(len(s)-len(p)+1):
                if set(s[i:i+len(p)]) == set(p):
                    indices.append(i)


        return indices