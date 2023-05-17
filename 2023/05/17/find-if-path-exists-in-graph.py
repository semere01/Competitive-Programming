from typing import List

class Solution:
    def initialialize(self, n):
        self.data = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.initialialize(n)
        for edge in edges:
            self.union(edge[0], edge[1])

        return self.rep(source) == self.rep(destination)
    
    def rep(self, n):
        n_rep = self.data[n]
        while n_rep != self.data[n_rep]:
            n_rep = self.data[n_rep]
        
        while n != self.data[n]:
            self.data[n] = n_rep
            n = self.data[n]

        return n_rep

    def union(self, n1, n2):
        n1_rep = self.rep(n1)
        n2_rep = self.rep(n2)
        if (n1_rep != n2_rep):
            if (self.size[n1_rep] > self.size[n2_rep]):
                self.data[n2_rep] = n1_rep
                self.size[n1_rep] += self.size[n2_rep]
            else:
                self.data[n1_rep] = n2_rep
                self.size[n2_rep] += self.size[n1_rep]
        


    

        n2_rep = self.data[n2]

        while n2_rep != self.data[n2_rep]:
            n2_rep = self.data[n2_rep]
        
        self.data[n1] = n2_rep

        # for i in range(len(self.data)):
        #     if (self.data[i] == n1):
        #         self.data[i] = n2_rep

