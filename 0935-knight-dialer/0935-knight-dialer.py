class Solution:
    def knightDialer(self, n: int) -> int:
        max_len = n
        MOD = 1000000007
        phone_dial = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9'],
            ['*', '0', '#']
        ]
        n, m = 4, 3
        valid_move = lambda x: 0 <= x[0] < n and 0 <= x[1] < m and phone_dial[x[0]][x[1]] != '*' and phone_dial[x[0]][x[1]] != '#'

        dp = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
        for i in range(n):
            for j in range(m):
                if (i, j) not in [(n-1, 0), (n-1, m-1)]:
                    dp[1][i][j] = 1

        for len_ in range(2, max_len+1):
            for i in range(n):
                for j in range(m):
                    if (i, j) not in [(n-1, 0), (n-1, m-1)]:
                        for dr, dc in [(2, 1), (2, -1), (-2, 1), (-2, -1), 
                                        (1, 2), (-1, 2), (1, -2), (-1, -2)]:
                            new_i, new_j = i+dr, j+dc
                            if valid_move((new_i, new_j)):
                                dp[len_][i][j] += dp[len_-1][new_i][new_j]

        return sum(dp[max_len][i][j] for i in range(n) for j in range(m)) % MOD      