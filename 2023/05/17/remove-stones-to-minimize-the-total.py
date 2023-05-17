import heapq
import math
from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        total = sum(piles)
        heap = []
        for pile in piles:
            heapq.heappush(heap, -1 * pile)
        for i in range(k):
            current = -1 * heapq.heappop()
            if (current == 0):
                break
            dec = current // 2
            if total <= dec:
                return 0
            total -= dec
            current -= dec
            heapq.heappush(-1 * current)
        
        return total


