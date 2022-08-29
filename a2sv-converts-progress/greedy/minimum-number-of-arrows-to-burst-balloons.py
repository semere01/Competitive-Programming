class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        if not points: return 0
        points.sort()
        prev = points[0]
        arrows = 1
        for s,e in points[1:]:
            if s > prev[1]:
              prev = [s, e]
              arrows += 1
            else:
              prev[1] = min(prev[1],e)
        return arrows


tests = [
    # [[10, 16], [2, 8], [1, 6], [7, 12]],
    # [[1, 2], [3, 4], [5, 6], [7, 8]],
    # [[1, 2], [2, 3], [3, 4], [4, 5]],
    [[3, 9], [7, 12], [3, 8], [6, 8], [9, 10],
        [2, 9], [0, 9], [3, 9], [0, 6], [2, 8]] # expected - 2
    # [[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]]
]

for t in tests:
    print(Solution().findMinArrowShots(t))
