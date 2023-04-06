class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        data = [0 for i in range(n)]
        for edge in edges:
            fro = edge[0]
            to = edge[1]
            data[to] = 1
        
        sources = []
        for datum_index in range(len(data)):
            datum = data[datum_index]
            if datum == 0:
                sources.append(datum_index)
        
        return sources
