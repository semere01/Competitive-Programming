class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        # Set Limits
        self.left_limit = -1
        self.right_limit = len(matrix[0])
        self.top_limit = -1
        self.bottom_limit = len(matrix)

        self.direction = "RIGHT"
        new_matrix = []
        p = (0, 0)  # r, c

        while len(new_matrix) < len(matrix) * len(matrix[0]):
            new_matrix.append(matrix[p[0]][p[1]])
            p = self.push(p)
        return new_matrix

    def push(self, pointer):
        if self.direction == "RIGHT":
            if pointer[1]+1 < self.right_limit:
                return (pointer[0], pointer[1]+1)
            else:
                self.direction = "DOWN"
                self.top_limit += 1
                return (pointer[0]+1, pointer[1])
        elif self.direction == "DOWN":
            if pointer[0]+1 < self.bottom_limit:
                return (pointer[0]+1, pointer[1])
            else:
                self.direction = "LEFT"
                self.right_limit -= 1
                return (pointer[0], pointer[1]-1)
        elif self.direction == "LEFT":
            if pointer[1]-1 > self.left_limit:
                return (pointer[0], pointer[1]-1)
            else:
                self.direction = "UP"
                self.bottom_limit -= 1
                return (pointer[0]-1, pointer[1])
        elif self.direction == "UP":
            if pointer[0]-1 > self.top_limit:
                return (pointer[0]-1, pointer[1])
            else:
                self.direction = "RIGHT"
                self.left_limit += 1
                return (pointer[0], pointer[1]+1)
