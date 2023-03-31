class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = (n % 2 != 0)
        while n != 0 and prev ^ (n % 2 == 0):
            prev = (n % 2 == 0)
            n = n >> 1
        return n == 0
