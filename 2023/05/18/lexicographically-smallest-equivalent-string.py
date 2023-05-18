class Union:
    def __init__(self, size=26):
        self.data = [i for i in range(size)]
    
    def rep(self, d):
        d_rep = self.data[d]

        while(self.data[d_rep] != d_rep):
            d_rep = self.data[d_rep]
        
        while(self.data[d] != d):
            next_pointer = self.data[d]
            self.data[d] = d_rep
            d = next_pointer
        
        return d_rep
    
    def union(self, d1 , d2):
        r1_rep = self.rep(ord(d1) - ord('a'))
        r2_rep = self.rep(ord(d2) - ord('a'))

        if r1_rep != r2_rep:
            if r1_rep < r2_rep:
                self.data[r2_rep] = r1_rep
            else:
                self.data[r1_rep] = r2_rep





class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        union = Union()
        for i in range(len(s1)):
            union.union(s1[i], s2[i])
        
        equivalent_string = []
        for s in baseStr:
            equivalent_string.append(chr(union.rep(ord(s) - ord('a'))+ord('a')))
        
        return ''.join(equivalent_string)
