class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:

        bestIndex = -1
        shortest_distance = 0

        for index in range(len(points)):
            point = points[index]
            if (x == point[0] or y == point[1]):
                man_distance = abs(x-point[0]) + abs(y-point[1])
                if (man_distance < shortest_distance or bestIndex == -1):
                    bestIndex = index
                    shortest_distance = man_distance

        return bestIndex
