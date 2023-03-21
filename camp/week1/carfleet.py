class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = sorted(zip(position, speed))
        fleets = [None] * n
        for i in range(n):
            time = (target - cars[i][0]) / cars[i][1]
            if i == n - 1 or time >= (target - cars[i + 1][0]) / cars[i + 1][1]:
                fleets[i] = True
        
        return fleets.count(True)
