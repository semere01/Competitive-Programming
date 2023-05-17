

class Union:
    def __init__(self, n):
        self.data = [i for i in range(n)]
        self.size = [1 for i in range(n)]
    
    def rep(self, n):
        n_rep = self.data[n]
        while(n_rep != self.data[n_rep]):
            n_rep = self.data[n_rep]

        while (n != self.data[n]):
            self.data[n] = n_rep
            n = self.data[n]
        
        return n_rep
    
    def union(self, n1, n2):
        n1_rep = self.rep(n1)
        n2_rep = self.rep(n2)
        if (n1_rep != n2_rep):
            # if n1 is bigger
            if (self.size[n1_rep] > self.size[n2_rep]):
                self.data[n2_rep] = n1_rep
                self.size[n1_rep] += self.size[n2_rep]
            else:
                self.data[n1_rep] = n2_rep
                self.size[n2_rep] += self.size[n1_rep]
            return True
        else:
            return False


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        union = Union(len(edges))
        for edge in edges:
            val = union.union(edge[0]-1, edge[1]-1)
            if (val == False):
                return edge
