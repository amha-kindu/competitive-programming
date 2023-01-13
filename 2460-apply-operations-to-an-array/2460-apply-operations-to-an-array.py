class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for num_idx in range(len(nums)-1):
            if nums[num_idx]==nums[num_idx+1]:
                nums[num_idx] *= 2
                nums[num_idx+1] = 0
                
        zero_ptr = 0
        while zero_ptr<len(nums):
            non_zero_ptr = zero_ptr
            while non_zero_ptr < len(nums) and nums[non_zero_ptr]==0:
                non_zero_ptr += 1
            
            if non_zero_ptr < len(nums):
                nums[zero_ptr], nums[non_zero_ptr] = nums[non_zero_ptr], nums[zero_ptr]
            
            zero_ptr += 1
            
        return nums
            