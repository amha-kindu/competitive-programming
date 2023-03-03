class Solution:
    def balancedString(self, s: str) -> int:
        count = Counter(s)
        n = len(s)
        min_len = n
        left = 0
        for right in range(n):
            count[s[right]]-=1
            while left < n and max(count.values()) <= n//4:
                min_len = min(min_len, right-left+1)
                count[s[left]]+=1
                left += 1
        return min_len



        