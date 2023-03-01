class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)-1
        new_matrix = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        for row_num in range(len(matrix)):
            for col_num in range(len(matrix[0])):
                new_row = col_num
                new_col = n-row_num
                new_matrix[new_row][new_col] = matrix[row_num][col_num]
        
        for row_num in range(len(matrix)):
            for col_num in range(len(matrix[0])):
                matrix[row_num][col_num] = new_matrix[row_num][col_num]



        """
        Do not return anything, modify matrix in-place instead.
        """