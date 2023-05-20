from collections import defaultdict
from typing import List


class Union:
    def __init__(self, size:int):
        self.data = [i for i in range(size)]
    
    def rep(self, x:int)->int:
        stack = [x]
        while(stack):
            current = stack[-1]
            if (current == self.data[current]):
                for element in stack:
                    self.data[element] = current
                return current
            else:
                stack.append(self.data[current])
    
    def join(self, x:int, y:int) -> None:
        x_rep = self.rep(x)
        y_rep = self.rep(y)

        self.data[x_rep] = y_rep




class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        s = list(s)
        union = Union(len(s))
        for pair in pairs:
            union.join(pair[0], pair[1])
        
        repToChildrenMap = defaultdict(list)
        for index, letter  in enumerate(s):
            rep = union.rep(index)
            repToChildrenMap[rep].append(letter)
        for rep in repToChildrenMap.keys():
            repToChildrenMap[rep].sort(reverse=True)
        ansList = []
        for index,letter in enumerate(s):
            letter_rep = union.rep(index)
            replacementLetter = repToChildrenMap[letter_rep].pop()
            ansList.append(replacementLetter)
        return ''.join(ansList)
        
        pass
        