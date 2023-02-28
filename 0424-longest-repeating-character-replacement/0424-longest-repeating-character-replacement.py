class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        count = defaultdict(int)

        left = 0
        max_len = 0
        mostFreq = 0
        for right in range(n):
            count[s[right]] += 1
            mostFreq = max(mostFreq, count[s[right]])
            while left < n and (right-left+1) - mostFreq > k:
                count[s[left]] -= 1
                left += 1

            max_len = max(max_len, right-left+1)
        return max_len