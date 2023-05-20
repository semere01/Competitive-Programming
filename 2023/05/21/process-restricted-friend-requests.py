from typing import List

class Union:
    def __init__(self, size:int, restrictions: list[list[int]]):
        self.data = [i for i in range(size)]
        self.restrictions = restrictions

    def rep(self, x: int) -> int:
        stack = [x]
        while stack:
            current = stack[-1]
            if self.data[current] == current:
                for element in stack:
                    self.data[element] = current
                return current
            else:
                stack.append(self.data[current])

    def validate(self, x_rep: int, y_rep: int) -> bool:
        for restriction in self.restrictions:
            l_left_rep = self.rep(restriction[0])
            r_left_rep = self.rep(restriction[1])
            if (x_rep == l_left_rep and y_rep == r_left_rep):
                return False
            if (y_rep == l_left_rep and x_rep == r_left_rep):
                return False
        return True

    def join(self, x: int, y: int):
        x_rep = self.rep(x)
        y_rep = self.rep(y)
        if (x_rep == y_rep):
            return True
        
        if self.validate(x_rep, y_rep):
            self.data[y_rep] = x_rep
            return True
        else:
            return False
        
        # if not self.validate(x_rep, y_rep):
        #     self.data[y_rep] = y_rep
        #     return False
        # else:
        #     return True

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        union = Union(n, restrictions)
        ansList = []
        for req in requests:
            ansList.append(union.join(req[0], req[1]))
        return ansList

# print(Solution().friendRequests(8, [[6,4],[7,5],[2,6],[1,5],[6,7],[6,5],[0,3],[5,4],[0,4],[2,7],[0,2]], [[6,3],[0,2],[0,5],[0,3],[6,4],[2,4],[1,0],[2,1],[2,5],[6,7],[7,0],[3,2],[3,5],[2,1],[1,6],[7,4],[6,3],[1,3],[6,5],[3,7],[7,0],[6,5],[0,5],[0,4],[7,5],[7,0],[7,0],[1,3]]))