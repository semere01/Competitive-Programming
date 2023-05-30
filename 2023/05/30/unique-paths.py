class Solution:
    def uqRec(self, m, n, x, y ,cache):
        if ((x,y) in cache):
            return cache[(x,y)]
        if (x == m-1 and y == n-1):
            return 1
        if x >= m or y >= n:
            cache[(x,y)] = 0
            return 0
        total = 0
        if (m-1 > x):
            total += self.uqRec(m, n, x+1, y,cache)
        if (n+1 > y):
            total += self.uqRec(m,n,x, y+1,cache)
        cache[(x,y)] = total
        return total


    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        return self.uqRec(m,n,0,0,cache)


for x in range(100):
    for y in range(100):
        (Solution().uniquePaths(x,y))
# print(c)