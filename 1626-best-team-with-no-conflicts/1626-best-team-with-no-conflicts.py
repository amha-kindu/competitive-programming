class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        players = []
        for i in range(n):
            players.append((scores[i], ages[i]))
        players.sort()

        dp = [players[i][0] for i in range(n)]
       
        for i in range(n):
            score_i, age_i = players[i]
            for j in range(i):
                score_j, age_j = players[j]
                if age_j <= age_i:
                    dp[i] = max(dp[i], dp[j]+score_i)
        
        return max(dp)