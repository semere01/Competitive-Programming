class Solution:
    def invert(self, n):
        string = ""
        for idx in range(len(n)):
            if n[idx] == "1":
                string += "0"
            else:
                string += "1" 
        return string
    def findSn(self, n, count): 
        newN = None
        if count > 0:
            newN = n + "1" + self.invert(n)[::-1]
            newN = self.findSn(newN, count - 1)
        else:
            newN = n
        return newN
    def findKthBit(self, n: int, k: int) -> str:
        sn = self.findSn("0", n)
        # print(sn)
        return sn[k-1]
