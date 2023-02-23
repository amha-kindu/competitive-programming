class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        leftSum = 0
        rightSum = sum(nums[1:])
        for i in range(n):
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
            if i+1 < n:
                rightSum -= nums[i+1]
        return -1