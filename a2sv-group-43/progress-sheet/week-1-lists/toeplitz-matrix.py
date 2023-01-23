class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:

        for row_num in range(len(matrix)):
            for col_num in range(len(matrix[0])):
                head_row_num = None
                head_col_num = None
                if (row_num > col_num):
                    head_col_num = 0
                    head_row_num = row_num - col_num
                else:
                    head_row_num = 0
                    head_col_num = col_num - row_num
                if matrix[row_num][col_num] != matrix[head_row_num][head_col_num]:
                    return False

        return True
