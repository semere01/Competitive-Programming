class Solution:
    def tribonacci(self, n: int) -> int:
        self.cache = {}
        return self.memo_fib(n)
        

    def memo_fib(self,n):
        if n <= 2:
            return min(n, 1)
        if n not in self.cache.keys():
            self.cache[n] = self.memo_fib(n-1) + self.memo_fib(n-2) + self.memo_fib(n-3)
        return self.cache[n]

