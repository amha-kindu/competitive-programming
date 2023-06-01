class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]
        grid[m-1][n-1]=1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i+1 < m:
                    grid[i][j] = grid[i+1][j]
                grid[i][j]+=grid[i][j+1] if j+1 < n else 0
        return grid[0][0]
        
        