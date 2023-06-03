class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = defaultdict(float)
        dp[(0, 0)] = poured
        
        for i in range(1, 100):
            for j in range(i+1):
                dp[(i, j)] = 0
                if dp[(i-1, j)] >= 1:
                    dp[(i, j)] = (dp[(i-1, j)] - 1) / 2
                if dp[(i-1, j-1)] >= 1:
                    dp[(i, j)] += (dp[(i-1, j-1)] - 1) / 2

            if (query_row, query_glass) in dp:
                return min( dp[(query_row, query_glass)], 1.0)