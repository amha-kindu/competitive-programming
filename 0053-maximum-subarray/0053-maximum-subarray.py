class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        prevSum=nums[0]
        maxSum=nums[0]
        for i in range(1, n):
            prevSum=max(nums[i], nums[i]+prevSum)
            maxSum = max(prevSum, maxSum)
        return maxSum