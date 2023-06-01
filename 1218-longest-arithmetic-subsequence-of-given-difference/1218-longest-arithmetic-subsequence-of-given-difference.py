class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(lambda: 1)
        answer = 0
        n = len(arr)
        for i in range(n):
            if arr[i] - difference in dp:
                dp[arr[i]] = dp[arr[i]-difference] + 1
            answer = max(answer, dp[arr[i]])
        return answer
