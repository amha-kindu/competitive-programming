class Solution:
    def removeDuplicates(self, nums) -> int:
        left = 0
        right = left + 1
        nums_len = len(nums)

        while True:

            while right<nums_len and nums[right]==nums[left]:
                right+=1

            if right < nums_len:
                nums[left+1] = nums[right]
            else:
                break

            left += 1

        return left+1
        
            