class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        duplicate = None
        for i in range(n):
            while nums[i]-1 != i and nums[i] != -1:
                if nums[i] != nums[nums[i]-1]:
                    nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
                else:
                    duplicate = nums[i]
                    nums[i] = -1

            if duplicate:
                break

        return duplicate