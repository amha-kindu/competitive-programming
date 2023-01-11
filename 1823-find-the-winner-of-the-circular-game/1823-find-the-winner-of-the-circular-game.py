class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if n==1:
            return 1;
        return (k-1 + self.findTheWinner(n-1, k)) % n + 1