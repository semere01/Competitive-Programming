class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        min_weight = max(weights)
        max_weight = sum(weights)
        while min_weight < max_weight:
            mid_weight = (min_weight + max_weight) // 2
            days_required = 1
            current_weight = 0
            for weight in weights:
                if current_weight + weight > mid_weight:
                    days_required += 1
                    current_weight = 0
                current_weight += weight  
            if days_required > D:
                min_weight = mid_weight + 1
            else:
                max_weight = mid_weight 
        return min_weight
