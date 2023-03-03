class Solution:
    def numMagicSquaresInside(self, grid):
        m = len(grid)
        n = len(grid[0])
        count = 0
        for row in range(m-2):
            for col in range(n-2):
                mainSum = -1
                miniGrid = set()
                complete = True
                for i in range(row,row+3):
                    total = 0
                    for j in range(col,col+3):
                        element = grid[i][j]
                        total += element
                        if element > 0 and element < 10:
                            miniGrid.add(element)
                    if mainSum == -1:
                        mainSum = total
                    else:
                        if mainSum != total:
                            complete = False
                            break
                for j in range(col,col+3):
                    total = 0
                    for i in range(row,row+3):
                        total += grid[i][j]
                    if mainSum == -1:
                        mainSum = total
                    else:
                        if mainSum != total:
                            complete = False
                            break
                total = 0
                j = col
                for i in range(row,row+3):
                    total += grid[i][j]
                    j += 1
                if mainSum == -1:
                    mainSum = total
                else:
                    if mainSum != total:
                        complete = False                            
                total = 0
                j = col + 2
                for i in range(row,row+3):
                    total += grid[i][j]
                    j -= 1
                if mainSum == -1:
                    mainSum = total
                else:
                    if mainSum != total:
                        complete = False                            
                if len(miniGrid)==9 and complete:
                    count += 1
        return count
