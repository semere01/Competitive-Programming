class Solution:
   def kthGrammar(self, N: int, K: int) -> int:
    if N == 1:
        return 0
    prev = self.kthGrammar(N-1, (K+1)//2)
    if K % 2 == 0:
        return 1 - prev
    else:
        return prev
