class Solution:
    def searchMatrix(self, data: list[list[int]], target: int) -> bool:
        min = 0
        max = len(data) * len(data[0]) - 1
        width = len(data[0])
        while min <= max:
            pointer = ((max-min)//2) + min
            if data[pointer // width][pointer % width] > target:
                max = pointer - 1
            elif data[pointer // width][pointer % width] < target:
                min = pointer + 1
            else:
                return True

        return False


tests = [
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),
    ([
        [1, 2, 3],
        [4, 5, 5],
        [5, 5, 6],
    ], 6, True),
    ([
        [1, 2, 3],
        [4, 7, 10],
        [834893274, 834893275, 834893290],
    ], 1, True),
    ([
        [1, 2, 3],
        [4, 5, 5],
        [5, 5, 5],
    ], 6, False),
    ([
        [1, 2, 3],
        [4, 7, 10],
        [834893274, 834893275, 834893290],
    ], 834893274, True),
    ([
        [1, 2, 3, 4, 5, 7, 8, 9, 10],
        [10, 10, 10, 10, 10, 10, 10, 10, 10],
        [834893274, 834893275, 834893290],
    ], 5, True),
    ([
        [1, 2, 3],
        [4, 7, 10],
        [834893274, 834893275, 834893290],
    ], 5, False),
    ([
        [1, 2, 3],
        [4, 7, 10],
        [834893274, 834893275, 834893290],
    ], 834893276, False),
]
counter = 0
for test in tests:
    counter += 1
    result = Solution().searchMatrix(test[0], test[1])
    if result != test[2]:
        print(f"Failed at test input {test[0]}, {test[1]}")
        break
    else:
        print(f"Test {counter}/{len(tests)} success")
