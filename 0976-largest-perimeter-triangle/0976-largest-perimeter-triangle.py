class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        is_valid = lambda x, y, z: x+y>z and y+z>x and x+z>y
        for i in range(len(nums)-1, 1, -1):
            if is_valid(nums[i], nums[i-1], nums[i-2]):
                return nums[i]+nums[i-1]+nums[i-2]
        return 0