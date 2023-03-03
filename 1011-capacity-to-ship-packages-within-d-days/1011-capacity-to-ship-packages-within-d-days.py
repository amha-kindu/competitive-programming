class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        low, high = max(weights), sum(weights)
        min_weight = low
        while high >= low:
            mid = ( low + high ) // 2
            days_ = 0
            weight = 0
            for i in range(n):
                days_ = float('inf') if weights[i] > mid else days_
                weight += weights[i]
                if i+1==n or weight + weights[i+1] > mid:
                    weight = 0
                    days_ += 1
            
            if days_ > days:
                low = mid + 1
            else:
                min_weight = mid
                high = mid - 1
        return min_weight