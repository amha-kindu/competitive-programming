class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        min_fall_sum = float('inf')
        dp = defaultdict(lambda: defaultdict(int))
        for i in range(n-1, -1, -1):
            for j in range(m):
                dp[i][j] = min(
                    dp[i+1][j-1] if j-1 >= 0 else float('inf'),
                    dp[i+1][j],
                    dp[i+1][j+1] if j+1 < m else float('inf')
                ) + matrix[i][j]
                if i == 0:
                    min_fall_sum = min(min_fall_sum, dp[i][j])
        return min_fall_sum
