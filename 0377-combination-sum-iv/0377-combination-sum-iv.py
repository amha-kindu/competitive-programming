class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        @lru_cache(None)
        def combo(sum_= 0):            
            if sum_ >= target:
                return int(sum_ == target)
            ans = 0
            for num in nums:
                ans += combo(sum_ + num)
            return ans
        return combo()