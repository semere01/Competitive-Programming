class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        transposed_matrix = []
        for x in range(len(matrix[0])):
            current_row = []
            for y in range(len(matrix)):
                current_row.append(matrix[y][x])
            transposed_matrix.append(current_row)

        return transposed_matrix
