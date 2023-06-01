class Solution:
    @lru_cache(None)
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return n
        answer = [0]*(n+1)
        answer[0] = 0
        answer[1] = 1
        i = 1
        while i <= n//2:
            answer[2 * i] = answer[i]
            if 2*i + 1 <= n:
                answer[2 * i + 1] = answer[i] + answer[i+1]
            i += 1
        
        return max(answer)