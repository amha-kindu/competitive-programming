class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return int(k != 1)

        half = 2**(n-1)
        if half >= k:
            return self.kthGrammar(n-1, k)
        else:
            return int(self.kthGrammar(n-1, k-half) != 1)