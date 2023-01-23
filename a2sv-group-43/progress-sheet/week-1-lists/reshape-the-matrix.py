from random import randint


class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        if (r*c != len(mat) * len(mat[0])):
            return mat

        input_width = len(mat[0])

        shifted = []

        for row_num in range(r):
            current_row = []
            for col_num in range(c):
                n = (row_num*c) + col_num
                current_row.append(mat[n//input_width][n % input_width])
            shifted.append(current_row)
        return shifted


test_count = 100
for test in range(test_count):
    # print("-" * 50)
    k = randint(2, 5)
    w = randint(1, 4) * k
    h = randint(1, 10)
    arr = []
    for i in range(h):
        c = []
        for j in range(w):
            c.append(randint(13, 44))
        arr.append(c)
    # for line in arr:
    #     print(line)
    # print(f"w - {k}, h - {int((w*h)/k)}")
    # print()
    x = Solution().matrixReshape(arr, k, int((w*h)/k))
    # for line in x:
    #     print(line)

    broken = False

    for i in range(w*h):
        if arr[i//w][i % w] != x[i // int((w*h)/k)][i % int((w*h)/k)]:
            broken = True
    if broken:
        print(f"test - {test+1}/{test_count} failed")
    else:
        print(f"test - {test+1}/{test_count} passed")
