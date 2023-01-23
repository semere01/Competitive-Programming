class Solution:
    def findLocal(self, grid, row_num, col_num):
        biggest = grid[row_num-1][col_num-1]
        for r in range(row_num-1, row_num+2):
            for c in range(col_num-1, col_num+2):
                if grid[r][c] > biggest:
                    biggest = grid[r][c]
        return biggest

    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        max_grid = []
        for row_num in range(1, len(grid) - 1):
            curr = []
            for col_num in range(1, len(grid[0]) - 1):
                curr.append(self.findLocal(grid, row_num, col_num))
            max_grid.append(curr)

        return max_grid
