class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_len = float('inf')
        left = 0
        right = 0
        wn_sum = nums[0]
        while left < n:
            while right < n and wn_sum<target:
                right += 1
                wn_sum += nums[right] if right<n else 0

            if right < n:
                min_len = min(min_len, right-left+1)
                
            wn_sum -= nums[left]
            left += 1
        
        min_len = 0 if min_len == float('inf') else min_len

        return min_len