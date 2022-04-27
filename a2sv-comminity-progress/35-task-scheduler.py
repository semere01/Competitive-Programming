class Solution:
    def leastInterval(self, threads, n) -> int:
        m = [0]*26;
        for letter in threads:
            m[ord(letter) - ord('A')] += 1
        m.sort()
        mostF = m[26 - 1] 
        c = (mostF - 1) * (n + 1)
        final = 0
        for n in m:
            if n == mostF:
                final += 1
        return max(c + final, len(threads))

