class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        p1Score, p2Score = sum(grid[0]), 0
        r2Score = float('inf')
        for i in range(n):
            p1Score -= grid[0][i]
            r2Score = min(r2Score, max(p1Score, p2Score))
            p2Score += grid[1][i]
            
        return r2Score