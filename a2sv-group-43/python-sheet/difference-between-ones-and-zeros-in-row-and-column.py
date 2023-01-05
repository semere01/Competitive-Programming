class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rowSums = []
        for rowIndex in range(len(grid)):
            rowSums.append(0)
            for colIndex in range(len(grid[0])):
                if grid[rowIndex][colIndex] == 0:
                    rowSums[rowIndex] -= 1
                else:
                    rowSums[rowIndex] += 1
        
        colSums = []
        for colIndex in range(len(grid[0])):
            colSums.append(0)
            for rowIndex in range(len(grid)):
                if grid[rowIndex][colIndex] == 0:
                    colSums[colIndex] -= 1
                else:
                    colSums[colIndex] += 1
        
        diffGrid = []
        for rowIndex in range(len(grid)):
            currentRow = []
            for colIndex in range(len(grid[0])):
                currentRow.append(rowSums[rowIndex] + colSums[colIndex])
            diffGrid.append(currentRow)
        
        return diffGrid













