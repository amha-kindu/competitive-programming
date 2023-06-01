class Solution:
    @lru_cache(None)
    def tribonacci(self, n: int) -> int:
        if n <= 2:
            return n % 2 + int(n == 2)
        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)