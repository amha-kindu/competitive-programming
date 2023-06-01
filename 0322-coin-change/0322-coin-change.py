class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = defaultdict(lambda : float('inf'))
        dp[0] = 0
        money = min(coins)
        while money <= amount:
            minimum = float('inf')
            for coin in coins:
                minimum = min(minimum, dp[money-coin])
            if minimum != float('inf'):
                dp[money] = minimum + 1
            money += 1
        
        return dp.get(amount, -1)