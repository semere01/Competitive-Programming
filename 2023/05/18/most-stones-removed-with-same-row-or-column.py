from collections import defaultdict


class Union:
    def __init__(self, dataList):
        self.data = {}
        for datum in dataList:
            self.data[datum] = datum
    
    def rep(self, x):
        x_rep = self.data[x]
        while (x_rep != self.data[x_rep]):
            x_rep = self.data[x_rep]
        
        while (x != self.data[x]):
            next_pointer = self.data[x]
            self.data[x] = x_rep
            x = next_pointer
        
        return x_rep
    
    def union(self , x, y):
        x_rep = self.rep(x)
        y_rep = self.rep(y)

        if (x_rep != y_rep):
            self.data[x_rep] = y_rep


class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        stones = [tuple(stone) for stone in stones]
        union = Union(stones)
        row_list = defaultdict(list)
        col_list = defaultdict(list)
        for stone in stones:
            row_list[stone[0]].append(stone)
            col_list[stone[1]].append(stone)
        
        for row in row_list.values():
            first = row[0]
            for el in row:
                union.union(first, el)
        for col in col_list.values():
            first = col[0]
            for el in col:
                union.union(first, el)
        
        head_set = set()
        for stone in stones:
            head_set.add(union.rep(stone))
        
        return len(stones) - len(head_set)
            
        

