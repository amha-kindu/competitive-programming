class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) <= 4:
            return 0
        else:
            return min(
                nums[-1] - nums[3],
                nums[-4] - nums[0],
                nums[-2] - nums[2],
                nums[-3] - nums[1]
            )