class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        @lru_cache(None)
        def robHouse(i=0):
            if i >= n-1:
                return 0
            return max( robHouse(i+2)+nums[i], robHouse(i+1) )

        @lru_cache(None)
        def robHouseReverse(i=n-1):
            if i < 1:
                return 0
            return max( robHouseReverse(i-2)+nums[i], robHouseReverse(i-1) )
        if n == 1:
            return nums[0]
        return max(robHouse(), robHouseReverse())