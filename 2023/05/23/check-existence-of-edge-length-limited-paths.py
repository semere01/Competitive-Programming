from collections import defaultdict
from typing import List


class Union:
    def __init__(self, size: int):
        self.data = [i for i in range(size)]

    def rep(self, x: int) -> int:
        stack = [x]
        while (stack):
            current = stack[-1]
            if (current == self.data[current]):
                for el in stack:
                    self.data[el] = current
                return current
            else:
                stack.append(self.data[current])

    def sameRep(self, x: int, y: int):
        return self.rep(x) == self.rep(y)

    def union(self, x: int, y: int):
        x_rep = self.rep(x)
        y_rep = self.rep(y)

        if (x_rep != y_rep):
            self.data[x_rep] = self.data[y_rep]


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        union = Union(n)
        edgeList.sort(key=lambda x: x[2])
        sortedQueries = sorted(queries, key=lambda x: x[2])
        edgePointer = 0
        queryPointer = 0
        answerList = []
        while queryPointer < len(sortedQueries):
            current_query = sortedQueries[queryPointer]
            while (edgePointer < len(edgeList) and edgeList[edgePointer][2] < current_query[2]):
                current_edge = edgeList[edgePointer]
                union.union(current_edge[0], current_edge[1])
                edgePointer += 1
            answerList.append(union.sameRep(current_query[0], current_query[1]))
            queryPointer += 1


        mymap = {tuple(query):answer for query, answer in zip(sortedQueries, answerList)}
        return [mymap[tuple(q)] for q in queries]


