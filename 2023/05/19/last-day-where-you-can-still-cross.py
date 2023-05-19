from typing import List


class Union:
    def __init__(self, r, c):
        self.data = [i for i in range(r*c)]
        self.rows = [set([i//c]) for i in range(r*c)]
        self.rowCount = r
    
    def rep(self, x):
        x_rep = self.data[x]
        while (x_rep != self.data[x_rep]):
            x_rep = self.data[x_rep]
        
        while(x != self.data[x]):
            next_pointer = self.data[x]
            self.data[x] = x_rep
            x = next_pointer
        
        return x_rep
    
    def union(self, x1, x2):
        x1_rep = self.rep(x1)
        x2_rep = self.rep(x2)

        if (x1_rep != x2_rep):
            self.data[x1_rep] = x2_rep
            self.rows[x2_rep] = self.rows[x2_rep].union(self.rows[x1_rep])
            if (len(self.rows[x2_rep]) == self.rowCount):
                return True
        return False

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        union = Union(row, col)

        landCells = set()
        for counter in range(len(cells)-1, -1, -1):
            currentRow = cells[counter][0] -1 
            currentCol = cells[counter][1] -1 
            currentCellNumber = (currentRow * col) + currentCol

            landCells.add(currentCellNumber)

            if currentRow + 1 < row and ((currentRow + 1)*col + currentCol) in landCells:
                nextCellNumber =  (currentRow + 1)*col + currentCol 
                if union.union(currentCellNumber, nextCellNumber):
                    break

            if currentRow - 1 >= 0 and ((currentRow - 1)*col + currentCol) in landCells:
                nextCellNumber =  (currentRow - 1)*col + currentCol 
                if union.union(currentCellNumber, nextCellNumber):
                    break

            if currentCol +1 < col and ((currentRow )*col + currentCol +1) in landCells:
                nextCellNumber =  (currentRow )*col + currentCol +1
                if union.union(currentCellNumber, nextCellNumber):
                    break

            if currentCol - 1 >= 0 and ((currentRow)*col + currentCol -1) in landCells:
                nextCellNumber =  (currentRow )*col + currentCol -1
                if union.union(currentCellNumber, nextCellNumber):
                    break
            
        #     print(union.rows)
        # return (row * col) - counter - 1
        return counter

print(Solution().latestDayToCross(6,2,[[4,2],[6,2],[2,1],[4,1],[6,1],[3,1],[2,2],[3,2],[1,1],[5,1],[5,2],[1,2]]))