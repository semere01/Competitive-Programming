from collections import deque
from typing import List


class Solution:
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        stage = deque([])
        for index, adjList in enumerate(adj):
            if len(adjList) == 1:
                stage.append(index)

        while (stage):
            current_head = stage.popleft()

            for child in adj[current_head]:
                adj[child].remove(current_head)
                adj[current_head].remove(child)
                if len(adj[child]) == 1:
                    stage.append(child)

        for adjList in adj:
            if adjList:
                return True

        return False
