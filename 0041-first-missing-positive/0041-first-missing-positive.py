class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(filter(lambda x: x >= 0, nums))
        n = len(nums)
        for i in range(n):
            while nums[i]-1 != i and nums[i]!=-1:
                if 0 <= nums[i]-1 < n and nums[i]!=nums[nums[i]-1]:
                    nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
                else:
                    nums[i] = -1
                
        for i in range(n):
            if nums[i] == -1:
                return i+1
                
        if nums:
            return nums[-1]+1
        else:
            return 1