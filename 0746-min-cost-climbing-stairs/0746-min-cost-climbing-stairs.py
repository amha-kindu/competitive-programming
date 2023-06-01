class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        @lru_cache(None)
        def topCost(n):
            if n >= len(cost):
                return 0
            return min(topCost(n+2), topCost(n+1)) + cost[n]

        return min(topCost(0), topCost(1))