class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        n = len(triangle)
        @lru_cache(None)
        def minPathSum(depth=0, i=0):
            if depth == n or i == len(triangle[depth]):
                return 0

            return min(
                minPathSum(depth+1, i+1),
                minPathSum(depth+1, i)
            ) + triangle[depth][i]

        return minPathSum()
