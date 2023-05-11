class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        reverseGraph = {}
        for edge in edges:
            currList = reverseGraph.get(edge[1], [])
            currList.append(edge[0])
            reverseGraph[edge[1]] = currList
        
        visited = set()
        
        def dfs(n, l):
            if n not in visited:
                visited.add(n)
                children = reverseGraph.get(n, [])
                for child in children:
                    l.add(child)
                    dfs(child, l)
                return l
        
        returnList = []
        for i in range(n):
            returnList.append(sorted(list(dfs(i, set()))))
            visited = set()
        
        return returnList