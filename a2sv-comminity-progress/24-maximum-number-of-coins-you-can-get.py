class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        sortedPiles = sorted(piles)
        l = len(piles)
        total = 0
        for i in range(int(l/3), l-1, 2):
            total += sortedPiles[i] 
        return total
