class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if not s:
            return t
        presenceMap = {}
        for index in range(ord('a'), ord('z')+1):
            letter = chr(index)
            presenceMap[letter] = 0

        for letter in s:
            presenceMap[letter] += 1

        for letter in t:
            if presenceMap[letter] == 0:
                return letter
            else:
                presenceMap[letter] -= 1
