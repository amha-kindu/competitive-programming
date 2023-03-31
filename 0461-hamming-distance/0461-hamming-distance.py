class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        cnt = 0
        num = x ^ y
        while num != 0:
            cnt += 1
            num = num & (num-1)
        return cnt