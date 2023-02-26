class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        # Initialize the cumulative sums for each row of the matrix
        self.cumulative_sums = []
        for row in matrix:
            cumulative_sum_row = [0]
            for num in row:
                cumulative_sum_row.append(cumulative_sum_row[-1] + num)
            self.cumulative_sums.append(cumulative_sum_row)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Calculate the sum of the region using the cumulative sums
        region_sum = 0
        for row in range(row1, row2 + 1):
            region_sum += self.cumulative_sums[row][col2 + 1] - self.cumulative_sums[row][col1]
        return region_sum
