from collections import defaultdict, deque
from typing import List


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        poorPoints = defaultdict(set)
        incomingCount = [0 for _ in range(len(quiet))]

        for edge in richer:
            poorPoints[edge[1]].add(edge[0])
            incomingCount[edge[0]] += 1 
        
        loudest = [-1 for _ in range(len(quiet))]

        def dfs(n):
            if loudest[n] == -1:
                d = [n]
                for child in poorPoints[n]:
                    d.append(dfs(child))
                loudest[n] = min(d, key=lambda x: quiet[x])
            return loudest[n]
        
        for i in range(len(incomingCount)):
            if not incomingCount[i]:
                dfs(i)
        return loudest

        # outgoingSets = defaultdict(set)
        # incomingCount = [0] * len(quiet)

        # for edge in richer:
        #     poortPoint
        #     outgoingSets[edge[0]].add(edge[1])
        #     incomingCount[edge[1]] +=1 
        
        # stage = deque()
        # for person in range(len(quiet)):
        #     if incomingCount[person] == 0:
        #         stage.append(person)
        # loudest = stage[0]
        # for rich_person in stage:
        #     if quiet[rich_person] < quiet[loudest]:
        #         loudest = rich_person
        
        # louder_list = [-1] * len(quiet)

        # stage_end = len(stage)
        # progress = 0

        # while stage:
        #     if (progress == stage_end):
        #         for rich_person in stage:
        #             if quiet[rich_person] < quiet[loudest]:
        #                 loudest = rich_person
        #         stage_end = len(stage)
        #         progress = 0
        #     current = stage.popleft()
        #     progress += 1
        #     louder_list[current] = loudest

        #     for child in outgoingSets[current]:
        #         incomingCount[child] -= 1
        #         if incomingCount[child] == 0:
        #             stage.append(child)
        
        # return louder_list
            
            
        