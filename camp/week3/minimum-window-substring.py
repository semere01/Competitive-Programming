class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        freq_map = {}
        for c in t:
            if c not in freq_map:
                freq_map[c] = 0
            freq_map[c] += 1
        
        best = ''
        left, right = 0, len(t)
        # print(freq_map)/
        for i in range(right):
            if s[i] in freq_map:
                freq_map[s[i]] -= 1
        # print(freq_map)

        if all(map(lambda x: x <= 0, freq_map.values())):
            return s[left:right]

        while right < len(s):
            # print(left, right, freq_map)
            if s[right] in freq_map:
                freq_map[s[right]] -= 1
            right += 1

            while all(map(lambda x: x <= 0, freq_map.values())):
                best = s[left:right] if not best or right-left < len(best) else best
                if s[left] in freq_map:
                    freq_map[s[left]] += 1
                left+=1
        while left < len(s) - len(t)+1:
            # print(left, right, freq_map)
            if s[left] in freq_map:
                freq_map[s[left]] += 1
            left+=1
            if all(map(lambda x: x <= 0, freq_map.values())):
                best = s[left:right] if not best or right-left+1 < len(best) else best
        # if not all(map(lambda x: x <= 0, freq_map.values())) and best == s:
        #     return ''
        return best
        















        # tmap = defaultdict(int)
        # for c in t:
        #     tmap[c] += 1

        # i, j = 0, len(t)

        # smap = defaultdict(int)

        # for c in s[i:j]:
        #     smap[c] += 1

        # besti, bestj = -1, -1
        # minwindow = 2e32
        # while j < len(s):
        #     # print(i, j)
        #     if all(map(lambda k: smap[k] >= tmap[k], tmap.keys())):
        #         while i < j and all(map(lambda k: smap[k] >= tmap[k], tmap.keys())):
        #             smap[s[i]] -= 1
        #             i += 1
        #         if j-i-1 < minwindow:
        #             minwindow = j-i-1
        #             besti, bestj = i-1, j 
        #         # print(besti, bestj)
        #     else:
        #         smap[s[j]] += 1
        #         j += 1
        # while all(map(lambda k: smap[k] >= tmap[k], tmap.keys())):
        #     smap[s[i]] -= 1
        #     i += 1
        # if j-i-1 < minwindow:
        #     minwindow = j-i-1
        #     besti, bestj = i-1, j

        # if not besti == -1:
        #     return s[besti:bestj]
        # else:
        #     return ""
        