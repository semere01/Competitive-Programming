class Solution:
    def reverseString(self, s: list[str]) -> None:
        self.s = s
        self.reverseInPlace(0,len(s)-1)

    def reverseInPlace(self, init, final):
        if final <=  init:
            return
        self.s[init], self.s[final] = self.s[final], self.s[init]
        self.reverseInPlace(init + 1, final - 1)

#hi
print(Solution().reverseString(["h","e","l","l","o"]))

