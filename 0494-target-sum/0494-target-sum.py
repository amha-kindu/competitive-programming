class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        @lru_cache(None)
        def backtrack(i=0, sum_=0):

            if i == n:
                return 1 if sum_ == target else 0

            return backtrack(i+1, sum_+nums[i]) + backtrack(i+1, sum_-nums[i])

        return backtrack()