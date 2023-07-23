class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        score = 0
        dp = defaultdict(int)
        for i in range(1, n):
            dp[i] = max(dp[i-1]-values[i-1]+i-1, values[i-1] + i - 1) + values[i] - i
            score = max(score, dp[i])
        return score