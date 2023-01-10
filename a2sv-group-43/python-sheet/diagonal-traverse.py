class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        data = []
        direction = "top-right"

        n = len(mat)
        m = len(mat[0])
        x, y = 0, 0
        while x < m and y < n:
            data.append(mat[y][x])
            if (y == n-1 and direction == "bottom-left"):
                x += 1
                direction = "top-right"
            elif (y == 0 and direction == "top-right"):
                if (x == m-1):
                    y += 1
                else:
                    x += 1
                direction = "bottom-left"
            elif (x == 0 and direction == "bottom-left"):
                y += 1
                direction = "top-right"
            elif (x == m-1 and direction == "top-right"):
                y += 1
                direction = "bottom-left"
            else:
                if (direction == "bottom-left"):
                    x -= 1
                    y += 1
                else:
                    x += 1
                    y -= 1

        return data
