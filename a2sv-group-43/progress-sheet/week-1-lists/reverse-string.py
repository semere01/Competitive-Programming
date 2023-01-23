class Solution:
    def reverseString(self, s: list[str]) -> None:
        p1 = len(s) - 1
        p2 = 0
        while (p1 > p2):
            s[p1], s[p2] = s[p2], s[p1]
            p1 -= 1
            p2 += 1
