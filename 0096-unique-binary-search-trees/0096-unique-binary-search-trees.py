class Solution:
    def numTrees(self, n: int) -> int:
        dp = defaultdict(lambda: 0)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            for j in range(i+1):
                dp[i] += dp[j] * dp[i-j-1]
        return dp[n]