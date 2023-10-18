class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 1000000007
        return (pow(4, n // 2, MOD) * pow(5, ceil(n / 2), MOD)) % 1000000007
        