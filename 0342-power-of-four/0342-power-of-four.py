class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        log4 = log(n) / log(4)
        return int(log4) == log4