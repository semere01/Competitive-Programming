class Solution:
    def validTicTacToe(self, board: list[str]) -> bool:
        board = [list(board_row) for board_row in board]

        x_count = 0
        o_count = 0
        for row in board:
            for cell in row:
                if cell == "X":
                    x_count += 1
                elif cell == "O":
                    o_count += 1

        if (self.o_wins(board) and self.x_wins(board)):
            return False
        if (o_count == x_count and self.x_wins(board)):
            return False
        if (o_count+1 == x_count and self.o_wins(board)):
            return False
        if o_count == x_count or o_count == x_count-1:
            return True
        return False

    def o_wins(self, board):
        wins = 0
        flush = ["O", "O", "O"]
        for row in board:
            if row == flush:
                wins += 1

        for i in range(3):
            temp = [board[0][i], board[1][i], board[2][i]]
            if temp == flush:
                wins += 1
        if [board[0][0], board[1][1], board[2][2]] == flush:
            wins += 1
        if [board[2][0], board[1][1], board[0][2]] == flush:
            wins += 1
        return bool(wins)

    def x_wins(self, board):
        wins = 0
        flush = ["X", "X", "X"]
        for row in board:
            if row == flush:
                wins += 1

        for i in range(3):
            if [board[0][i], board[1][i], board[2][i]] == flush:
                wins += 1
        if [board[0][0], board[1][1], board[2][2]] == flush:
            wins += 1
        if [board[2][0], board[1][1], board[0][2]] == flush:
            wins += 1
        return bool(wins)


print(Solution().validTicTacToe(["XXX", "XOO", "OO "]))
# ["XXX","XOO","OO "]
