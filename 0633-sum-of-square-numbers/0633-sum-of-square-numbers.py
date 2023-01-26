class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        for i in range(int(sqrt(c))+1):
            other = c - i**2
            if floor(sqrt(other))==ceil(sqrt(other)):
                return True
        return False
            