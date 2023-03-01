class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        num_map = [0] * 1001

        for trip in trips:
            for point in range(trip[1], trip[2] ):
                num_map[point] += trip[0]
        
        return max(num_map) <= capacity


