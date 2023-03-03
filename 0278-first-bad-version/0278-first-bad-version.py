# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        firstBad = n
        left, right = 1, n
        while left <= right:
            mid = (left + right)//2
            if isBadVersion(mid):
                firstBad = mid
                right = mid-1
            else:
                left = mid + 1
        return firstBad
        