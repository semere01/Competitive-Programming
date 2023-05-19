class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [set() for i in range(n)]
        distances = [-1 for i in range(n)]
        for road in roads:
            if (distances[road[0]-1] == -1):
                distances[road[0]-1] = road[2]
            else:
                distances[road[0]-1] = min(road[2], distances[road[0]-1])
            if (distances[road[1]-1] == -1):
                distances[road[1]-1] = road[2]
            else:
                distances[road[1]-1] = min(road[2], distances[road[1]-1])
            graph[road[0]-1].add(road[1]-1)
            graph[road[1]-1].add(road[0]-1)
        visited = set()
        minDistance = distances[0]
        stack = [0]
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                children = graph[current]
                if distances[current] < minDistance:
                    minDistance = distances[current]
                for child in children:
                    if child not in visited:
                        stack.append(child)
                        # graph[current].remove(child)
                        # graph[child].remove(current)
        
        return minDistance
                

