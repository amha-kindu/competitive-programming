class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        fst_pos = bisect_left(nums, target)
        last_pos = bisect_right(nums, target)
        if fst_pos == len(nums) or nums[fst_pos] != target:
            return -1, -1
        else:
            return bisect_left(nums, target), bisect_right(nums, target)-1