class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while nums[i] != i and nums[i] != -1:
                if nums[i] < n:
                    nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
                else:
                    nums[i] = -1
        
        try:
            answer = nums.index(-1)
        except:
            answer = nums[-1] + 1
        
        return answer