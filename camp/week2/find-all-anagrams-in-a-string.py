class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        s = list(s)
        p = list(p)
        ord_a = ord('a')

        input_count_map = [0] * 26
        for letter in p:
            input_count_map[ord(letter) - ord_a] += 1
        
        sliding_count_map = [0] * 26
        for letter in range(len(p)):
            sliding_count_map[ord(letter) - ord_a] += 1
        
        anagram_count = []
        p0 = 0
        p1 = len(p)

        if (sliding_count_map) == input_count_map:
            anagram_count.append(0) 

        while p1 <= len(s):
            sliding_count_map[ord(s[p0-1]) - ord_a] -= 1
            sliding_count_map[ord(s[p1+1]) - ord_a] += 1
            if (sliding_count_map) == input_count_map:
                anagram_count .append(p0)
            p0 += 1
            p1 += 1
        
        return anagram_count
        

        
        


        indices = []
        s = list(s)
        p = set(p)
        p0 = 0
        p1 = len(p)
        while p1 <= len(s):
            curr = set(s[p0:p1])
            if curr == p:
                indices.append(p0)
            p1 += 1
            p0 += 1

        return indices


print(Solution().findAnagrams("baa", "aa"))
