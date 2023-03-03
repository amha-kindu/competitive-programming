class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 1:
            return ceil(piles[0]/h)

        low = 1
        high = max(piles)
        min_speed = low
        while high >= low:
            mid = ( low + high ) // 2
            time = 0
            for pile in piles:
                time += ceil(pile / mid)
            if time > h:
                low = mid + 1
            else:
                min_speed = mid
                high = mid - 1
        return min_speed

        