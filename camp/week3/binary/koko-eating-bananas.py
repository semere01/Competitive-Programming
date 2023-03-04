class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        left = 1
        right = max(piles)
        
        while left <= right:
            mid = left + (right - left) // 2
            total_time = sum(math.ceil(pile / mid) for pile in piles)
            
            if total_time > H:
                left = mid + 1
            else:
                right = mid - 1
        
        return left