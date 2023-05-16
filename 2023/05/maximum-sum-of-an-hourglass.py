class Solution:
    def maxSum(self, grid: list[list[int]]) -> int:
        biggestSum = 0
        for y in range(1, len(grid)-1):
            for x in range(1, len(grid[0]) - 1):
                current = self.calculateHourSum(grid, x, y)
                if current > biggestSum:
                    biggestSum = current

        return biggestSum

    def calculateHourSum(self, grid, x, y):
        topSum = grid[y-1][x-1] + grid[y-1][x] + grid[y-1][x+1]
        # bottomSum = grid[x-1][y+1] + grid[x][y+1] + grid[x+1][y+1]
        bottomSum = grid[y+1][x-1] + grid[y+1][x] + grid[y+1][x+1]
        total = topSum + grid[y][x] + bottomSum
        return total


test_case = [[6, 2, 1, 3], [4, 2, 1, 5], [9, 2, 8, 7], [4, 1, 2, 9]]
