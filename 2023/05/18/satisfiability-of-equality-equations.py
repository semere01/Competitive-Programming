class Union:
    def __init__(self, size = 26):
        self.data = [i for i in range(size)]
        self.size = [1 for i in range(size)]
    
    def rep(self, x):
        x = ord(x) - ord('a')
        x_rep = self.data[x]
        while (x_rep != self.data[x_rep]):
            x_rep = self.data[x_rep]
        
        while (x != self.data[x]):
            next_pointer = self.data[x]
            self.data[x] = x_rep
            x = next_pointer
        
        return x_rep
    
    def union(self, a, b):
        a_rep = self.rep(a)
        b_rep = self.rep(b)

        if (a_rep != b_rep):
            if self.size[a_rep] < self.size[b_rep]:
                self.data[b_rep] = a_rep
                self.size[a_rep] += self.size[b_rep]
            else:
                self.data[a_rep] = b_rep
                self.size[b_rep] += self.size[a_rep]



class Solution:
    def equationsPossible(self, equations: list[str]) -> bool:
        union = Union()
        for equataion in equations:
            if equataion[1] == "=":
                union.union(equataion[0], equataion[-1])
        for equataion in equations:
            if equataion[1] == "!":
                if (union.rep(equataion[0]) == union.rep(equataion[-1])):
                    return False
        
        return True


        pass

print(Solution().equationsPossible(["a==b","e==c","b==c","a!=e"]))