class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        def has_leading(x):
            i = 0
            while x[i] == 0:
                i += 1
            return i > 0

        @lru_cache(None)
        def countWays(i=0):
            if i >= n:
                return int(i==n)
            if s[i] == '0':
                return 0
            
            temp = countWays(i+1)
            if not has_leading(s[i: i+2]) and int(s[i: i+2]) < 27:
                temp += countWays(i+2)
            return temp

        return countWays()

