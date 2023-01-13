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
        total = topSum + grid[x][y] + bottomSum
        return total


# test_case = [[6, 2, 1, 3], [4, 2, 1, 5], [9, 2, 8, 7], [4, 1, 2, 9]]
test_case = [[520626, 685427, 788912, 800638, 717251, 683428], [23602, 608915,
                                                                697585, 957500, 154778, 209236], [287585, 588801, 818234, 73530, 939116, 252369,]]
print(Solution().maxSum(test_case))
