class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] != ".":
                    board[r][c] = int(board[r][c])
        for row_num in range(len(board)):
            non_zero_count = sum(1 for cell in board[row_num] if cell != ".")
            if (len(set([i for i in board[row_num] if i != '.'])) != non_zero_count):
                print("ping 0")
                return False

        for col_num in range(len(board[0])):
            non_zero_count = 0
            col_set = set()
            for row_num in range(len(board)):
                if board[row_num][col_num] != ".":
                    non_zero_count += 1
                    col_set.add(board[row_num][col_num])
            if (len(col_set) != non_zero_count):
                print("ping 1")
                return False

        region_map = [[] for i in range(9)]

        for row_num in range(9):
            for col_num in range(9):
                if (board[row_num][col_num] != "."):
                    region_map[board[row_num][col_num] -
                               1].append((row_num//3, col_num//3))

        for rm in region_map:
            if len(set(rm)) != len(rm):
                print("ping 2")
                return False

        return True


print(Solution().isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], [
      "4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
