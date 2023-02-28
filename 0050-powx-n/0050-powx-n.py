class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            x = 1/x
            n = abs(n)
        
        if n%2==0:
            m = self.myPow(x, n//2)
            return m*m
        else:
            m = self.myPow(x, n//2)
            return m*m*x