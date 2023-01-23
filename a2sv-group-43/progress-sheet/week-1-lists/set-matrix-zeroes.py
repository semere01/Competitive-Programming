class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        zero_rows = set()
        zero_cols = set()

        for row_num in range(len(matrix)):
            for col_num in range(len(matrix[0])):
                if matrix[row_num][col_num] == 0:
                    zero_rows.add(row_num)
                    zero_cols.add(col_num)

        for row_num in range(len(matrix)):
            for col_num in range(len(matrix[0])):
                if ((row_num in zero_rows) or (col_num in zero_cols)):
                    matrix[row_num][col_num] = 0
