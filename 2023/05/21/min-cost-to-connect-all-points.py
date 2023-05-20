

class Union:
    def __init__(self, size:int):
        self.data = [i for i in range(size)]

    def rep(self, x: int) -> int:
        stack = [x]
        while stack:
            current = stack[-1]
            if self.data[current] == current:
                # for element in stack:
                #     self.data[element] = current
                return current
            else:
                stack.append(self.data[current])


    def join(self, x: int, y: int):
        x_rep = self.rep(x)
        y_rep = self.rep(y)
        
        self.data[y_rep] = x_rep


class Solution:
    def manDistance(self, p1, p2):
        x = abs(p1[0] - p2[0])
        y = abs(p1[1] - p2[1])
        return x + y

    def minCostConnectPoints(self, points):
        distances = []
        union = Union(len(points))
        for x in range(len(points)):
            for y in range(len(points)):
                distances.append([x, y, self.manDistance(points[x], points[y])])

        distances.sort(key=lambda a: a[2])
        minCost = 0
        counter = 0

        for distance in distances:
            if union.rep(distance[0]) != union.rep(distance[1]):
                union.join(distance[0], distance[1])
                minCost += distance[2]
                counter += 1
                if counter == len(points) - 1:
                    break

        return minCost
