class Solution:
    def decodeString(self, s: str) -> str:
        self.nums = set([str(i) for i in range(10)])

        return self.decodeRight()
    
    # def decodeBrack(self, )
    

    def decodeRight(self, i):
        char = self.s[i]

        if i == len(s):
            return
        if (char == "[" or char == "]"):
            return self.decodeRight(i+1)
        if (char in self.nums):
            return eval(char) * (self.decodeRight(i+1))
        return char + self.decodeRight(i+1)

print(Solution().de)