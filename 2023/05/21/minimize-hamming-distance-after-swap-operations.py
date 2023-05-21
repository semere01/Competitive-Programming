from collections import defaultdict
from typing import List


class Union:
    def __init__(self, size: int):
        self.data = [i for i in range(size)]

    def rep(self, x: int) -> int:
        stack = [x]
        while (stack):
            current = stack[-1]
            if (self.data[current] == current):
                for element in stack:
                    self.data[element] = current
                return current
            else:
                stack.append(self.data[current])

    def join(self, x: int, y: int) -> None:
        x_rep = self.rep(x)
        y_rep = self.rep(y)

        self.data[x_rep] = self.data[y_rep]


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        union = Union(len(source))
        for pair in allowedSwaps:
            union.join(pair[0], pair[1])

        repToChildren = defaultdict[list]
        for index in range(len(source)):
            rep = union.rep(index)
            repToChildren[rep].append(index)

        hd = 0
        for rep in repToChildren.keys():
            sorted_source = [source[i] for i in repToChildren[rep]]
            sorted_target = [target[i] for i in repToChildren[rep]]
            hd += len(list(set(sorted_source) ^ set(sorted_target)))

        return hd

        pass
